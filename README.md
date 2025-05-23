
---

# DataTasker 🚀✨

## Core Functionality

**DataTasker** is a production-grade asynchronous CSV processing system built with FastAPI, Celery, Redis, and Pandas designed to deliver reliable, scalable, and traceable data insights. 📊⚡️

* **Asynchronous Processing ⏳🔄**
  Handles CSV file processing as background tasks using Celery and Redis, ensuring the API remains fast and responsive even under heavy load. 🚀

* **Data Cleaning and Validation 🧹✅**
  Automatically cleans incoming data by trimming whitespace, converting data types, dropping incomplete rows, and handling division by zero to maintain data integrity. 🛠️

* **Aggregation by Region 🌍📈**
  Summarizes sales data by calculating total and average revenue, total quantity sold, and average discount per region, enabling quick regional performance insights. 📉💡

* **Sensitive Anomaly Detection 🚨🔍**
  Calculates revenue per unit for each row and identifies anomalies using a configurable statistical threshold (mean + 2 \* standard deviation). This flags unusually high revenue-per-unit cases for further investigation. ⚠️🔬

* **Traceable Outputs 🗂️📅**
  Saves timestamped CSV files for both the regional summary and detected anomalies, providing audit trails and easy integration with downstream systems. 🧾🛡️

* **Task Tracking with ID 🧾📌**
  Returns the Celery task ID in the API response when a CSV file is uploaded, allowing clients to track the processing status and integrate job monitoring workflows. 🧭📬

* **Robust Error Handling 🛠️❗**
  Catches and reports exceptions cleanly to maintain system reliability and facilitate debugging. 🐞🔧

---

**DataTasker** focuses on scalability, maintainability, and operational transparency, making it an ideal core for any production data pipeline requiring asynchronous batch processing and sensitive anomaly detection. 🌟🔗

---
