from fastapi import FastAPI, Query
from app.downloader import get_video_formats, download_video
from app.models import DownloadRequest
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend origin
origins = ["*"]  # in production you should restrict to Vercel domain

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/formats")
async def formats(url: str = Query(...)):
    formats = get_video_formats(url)
    return formats

@app.post("/download")
async def download(req: DownloadRequest):
    message = download_video(req.url, req.itag)
    return {"message": message}
