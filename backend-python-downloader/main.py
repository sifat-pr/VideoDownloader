from fastapi import FastAPI
from models import DownloadRequest
from downloader import download_video

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is up."}

@app.post("/download")
def download(req: DownloadRequest):
    file_path = download_video(req.url, req.format_id, req.filename)
    return {"file_path": file_path}
