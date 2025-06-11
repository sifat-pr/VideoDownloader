from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yt_dlp
import os

app = FastAPI()

DOWNLOAD_DIR = "./downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

class DownloadRequest(BaseModel):
    url: str
    quality: str
    filename: str

@app.post("/download")
async def download_video(req: DownloadRequest):
    try:
        output_path = f"{DOWNLOAD_DIR}/{req.filename}.%(ext)s"
        ydl_opts = {
            'format': req.quality,
            'outtmpl': output_path,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(req.url, download=True)
        return {"status": "success", "title": info.get('title')}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/formats")
async def get_formats(url: str):
    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = [{
                'format_id': f['format_id'],
                'ext': f['ext'],
                'resolution': f.get('format_note', ''),
                'filesize': f.get('filesize', 0)
            } for f in info['formats'] if f.get('vcodec') != 'none']
            return formats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
