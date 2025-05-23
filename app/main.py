from fastapi import FastAPI, UploadFile, File
from celery.result import AsyncResult
import os
import shutil
from app.tasks.csv_processor import process_csv
from app.worker.celery_app import celery_app

app = FastAPI()

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    task = process_csv.delay(file_location)

    return {
        "message": f"File '{file.filename}' uploaded and processing started.",
        "task_id": task.id
    }


@app.get("/status/{task_id}")
def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)

    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None
    }
