#docker run -d --name fastapi_test -v /mnt/e/aigenda_drive/project_code/fastapi:/app -p 7000:9000 fastapi_test
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from youtube_downloader import YouTubeDownloader

app = FastAPI()

class DownloadRequest(BaseModel):
    url: str

downloader = YouTubeDownloader()

@app.post("/download/")
def download_video(request: DownloadRequest):
    try:
        downloader.download_video(request.url)
        return {"message": "Download successful", "file": downloader.download_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def run():
    uvicorn.run(app="app:app", host="0.0.0.0", port=7000, reload=True)

if __name__ == "__main__":
    run()