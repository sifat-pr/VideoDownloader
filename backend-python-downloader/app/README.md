# Backend Python Downloader

This service is responsible for downloading videos using yt-dlp and exposing a FastAPI server for handling download requests.

## Features
- Accepts video URL, quality, and format.
- Validates URLs.
- Downloads videos using yt-dlp.
- Saves files locally.
- Returns local file URL or stream link.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
