from fastapi import FastAPI, UploadFile, File, BackgroundTasks
import shutil
from processor import process_video_pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"status": "server is running"}

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    path = f"{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"video_path": path}

@app.post("/process-video")
async def process_video(video_path: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_video_pipeline, video_path)
    return {"status": "processing started"}
