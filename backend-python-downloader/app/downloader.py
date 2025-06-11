from pytube import YouTube
import os

DOWNLOAD_PATH = os.path.join(os.getcwd(), "downloads")

os.makedirs(DOWNLOAD_PATH, exist_ok=True)

def get_video_formats(url: str):
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True).order_by('resolution').desc()
    
    formats = []
    for stream in streams:
        formats.append({
            'itag': stream.itag,
            'resolution': stream.resolution,
            'mime_type': stream.mime_type,
            'filesize_mb': round(stream.filesize / (1024 * 1024), 2)
        })
    return formats

def download_video(url: str, itag: int):
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(itag)
    stream.download(output_path=DOWNLOAD_PATH)
    return f"{stream.title} downloaded successfully."
