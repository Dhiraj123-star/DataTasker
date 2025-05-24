
---

# DataTasker 🚀✨

## Core Functionality

**DataTasker** is a production-grade asynchronous CSV processing system built with **FastAPI**, **Celery**, **Redis**, **Pandas**, and **SQLite**, now with a **CI/CD pipeline** and **multi-stage Docker build** for efficient deployment. ⚙️📦

---

### ✅ Key Features

* **Asynchronous Processing ⏳🔄**
  Handles CSV file processing as background tasks using **Celery** and **Redis**, keeping the API fast and responsive under heavy load. 🚀

* **CI/CD Integration with GitHub Actions 🧪🚀**
  Automated testing and deployment pipeline built with GitHub Actions that publishes Docker images to [Docker Hub](https://hub.docker.com/repository/docker/dhiraj918106/datatasker), enabling continuous integration and delivery.

* **Multi-Stage Docker Build 🐳📦**
  Implements a production-ready multi-stage Dockerfile that reduces image size and improves build speed, making the deployment lighter and more efficient.

* **Data Cleaning and Validation 🧹✅**
  Trims whitespace, converts data types, drops incomplete rows, and handles division by zero to maintain clean, reliable data. 🛠️

* **Aggregation by Region 🌍📈**
  Summarizes sales data per region (total/average revenue, quantity sold, average discount) for performance insights. 📊

* **Sensitive Anomaly Detection 🚨🔍**
  Detects outliers based on revenue-per-unit using a statistical threshold (`mean + 2 × std`), flagging data that needs further review. ⚠️🔬

* **Traceable Outputs 🗂️📅**
  Saves results with filenames tied to Celery task IDs, supporting auditability and traceability. 🧾

* **Task Status Tracking with SQLite 🗃️📊**
  Logs task IDs, status, start and end timestamps, and processing duration to a **SQLite** database for persistent tracking and reporting. 📋🔍

* **Result Retrieval & Download API 📥🗂️**
  Enables download of generated CSV files (summary and anomalies) using the task ID through dedicated API endpoints. 🔄

* **Input Validation & Schema Enforcement 📊🔍**
  Checks uploaded CSV files for required columns and valid formatting before processing. ✅

* **Robust Error Handling 🛠️❗**
  Gracefully catches and logs errors during data processing to prevent system failure and support debugging. 🐞🔧

---

**DataTasker** emphasizes **scalability**, **automation**, and **deployment-readiness**, making it an ideal foundation for any data-heavy system that demands background job execution, anomaly detection, and DevOps excellence. 🌐⚡

---
