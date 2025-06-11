from pydantic import BaseModel

class DownloadRequest(BaseModel):
    url: str
    format_id: str
    filename: str
