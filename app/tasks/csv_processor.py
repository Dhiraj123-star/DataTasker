from app.worker.celery_app import celery_app
import pandas as pd
import os
from datetime import datetime

@celery_app.task
def process_csv(file_path: str):
    try:
        # Ensure output directory exists
        output_dir = os.path.dirname(file_path)
        os.makedirs(output_dir, exist_ok=True)

        df = pd.read_csv(file_path)

        # Clean column names and types
        df.columns = [col.strip() for col in df.columns]
        df.dropna(inplace=True)
        df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
        df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
        df['discount'] = pd.to_numeric(df['discount'], errors='coerce')

        # Remove rows with zero quantity to avoid division by zero
        df = df[df['quantity'] != 0]

        # Aggregate by region
        region_summary = df.groupby('region').agg({
            'revenue': ['sum', 'mean'],
            'quantity': 'sum',
            'discount': 'mean'
        }).reset_index()

        # Anomaly Detection
        df['rev_per_unit'] = df['revenue'] / df['quantity']
        mean = df['rev_per_unit'].mean()
        std = df['rev_per_unit'].std()

        # Adjusted threshold (2 * std is less strict than 3 * std)
        threshold = mean + 2 * std
        df['is_anomaly'] = (df['rev_per_unit'] > threshold)

        # Save output files
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        base_name = os.path.splitext(file_path)[0]

        summary_file = f"{base_name}_region_summary_{timestamp}.csv"
        anomalies_file = f"{base_name}_anomalies_{timestamp}.csv"

        region_summary.columns = ['region', 'revenue_sum', 'revenue_mean', 'quantity_sum', 'discount_mean']
        region_summary.to_csv(summary_file, index=False)

        anomalies_df = df[df['is_anomaly']]
        if not anomalies_df.empty:
            anomalies_df.to_csv(anomalies_file, index=False)
        else:
            # Create an empty anomalies file for traceability
            pd.DataFrame(columns=df.columns).to_csv(anomalies_file, index=False)

        return {
            "status": "success",
            "region_summary": summary_file,
            "anomalies": anomalies_file,
            "threshold": threshold,
            "mean_rev_per_unit": mean,
            "std_rev_per_unit": std,
            "total_anomalies": int(df['is_anomaly'].sum())
        }

    except Exception as e:
        return {"status": "failed", "error": str(e)}
