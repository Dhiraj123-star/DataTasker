from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from celery.result import AsyncResult
import os
import shutil
from app.tasks.csv_processor import process_csv  # Import the task directly

app = FastAPI()

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
    finally:
        await file.close()

    task = process_csv.delay(file_location)

    return {
        "message": f"File '{file.filename}' uploaded and processing started.",
        "task_id": task.id
    }

@app.get("/status/{task_id}")
def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=process_csv.app)

    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None
    }

@app.get("/download/summary/{task_id}")
def download_summary(task_id: str):
    file_path = os.path.join(UPLOAD_DIR, f"sales_data_region_summary_{task_id}.csv")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Summary file not found.")
    return FileResponse(file_path, media_type="text/csv", filename=os.path.basename(file_path))

@app.get("/download/anomalies/{task_id}")
def download_anomalies(task_id: str):
    file_path = os.path.join(UPLOAD_DIR, f"sales_data_anomalies_{task_id}.csv")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Anomalies file not found.")
    return FileResponse(file_path, media_type="text/csv", filename=os.path.basename(file_path))
