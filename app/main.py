from fastapi import FastAPI,UploadFile,File
import os
import shutil
from app.tasks.csv_processor import process_csv

app = FastAPI()

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR,exist_ok=True)

@app.post("/upload/")
async def upload_file(file:UploadFile=File(...)):
    file_location=os.path.join(UPLOAD_DIR,file.filename)

    with open(file_location,"wb") as f:
        shutil.copyfileobj(file.file,f)
    
    process_csv.delay(file_location)

    return {"message":f"File '{file.filename}' uploaded and processing started."}

    
