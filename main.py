from fastapi import FastAPI
from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
# from utils.watermark_removal_pytorch.api import remove_watermark
import uvicorn
import os

app = FastAPI()

MEDIA_ROOT = "media"

@app.post("/upload")
def upload(image: UploadFile = File(...), mask: UploadFile = File(...)):
    try:
        with open(os.path.join(MEDIA_ROOT, image.filename), 'wb') as f:
            f.write(image.file.read())
        with open(os.path.join(MEDIA_ROOT, mask.filename), 'wb') as f:
            f.write(mask.file.read())
    except Exception:
        return {"message": "There was an error uploading files"}
    finally:
        image.file.close()
        mask.file.close()

    return {"message": f"Successfully uploaded {image.filename}, {mask.filename}"}


@app.get("/")
async def main():
    content = """
<body>
<form action="/upload/" enctype="multipart/form-data" method="post">
<input name="image" type="file">
<input name="mask" type="file">
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)