import yt_dlp
import os

def download_video(url: str, format_id: str, filename: str) -> str:
    output_path = f"downloads/{filename}.%(ext)s"
    
    ydl_opts = {
        'format': format_id,
        'outtmpl': output_path,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)
    return file_path
