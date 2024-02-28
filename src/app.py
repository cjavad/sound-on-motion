from typing import Annotated
from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .consts import ACTIVE_SOUND_FILE, SOUND_PATH, STATIC_PATH, TEMPLATE_PATH
from .models import ActiveSound, SoundFile


app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")
templates = Jinja2Templates(directory=TEMPLATE_PATH)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("views/index.html", {"request": request})

@app.get("/sounds")
async def sounds(request: Request):
    active_sound = ActiveSound()
    sounds = [sound.name for sound in SOUND_PATH.glob("*.*")]
    sounds = [ SoundFile(id=n, filename=n, is_active=n == active_sound.active_sound) for n in sounds ]
    
    return templates.TemplateResponse("views/sounds.html", {"request": request, "sounds": sounds})

@app.post("/delete")
async def delete_sound(request: Request, sound_id: Annotated[str, Form()]):
    sound_file = SOUND_PATH / sound_id
    if sound_file.exists():
        sound_file.unlink()
        return templates.TemplateResponse("views/status.html", {"request": request, "info": f"file '{sound_id}' deleted"})
    else:
        return templates.TemplateResponse("views/status.html", {"request": request, "status_code": 404, "status_message": f"file '{sound_id}' not found"}, status_code=404)

@app.get("/upload")
async def upload_page(request: Request):
    return templates.TemplateResponse("views/upload.html", {"request": request})

@app.post("/upload")
async def upload(request: Request, file: UploadFile = File(...)):
    try:
        file_path = SOUND_PATH / file.filename
        with open(file_path, "wb+") as file_object:
            file_object.write(file.file.read())
        return templates.TemplateResponse("views/status.html", {"request": request, "info": f"file '{file.filename}' saved at '{file_path}'"})
    except Exception as e:
        return templates.TemplateResponse("views/status.html", {"request": request, "status_code": 500, "status_message": str(e)}, status_code=500)


@app.post("/set_active")
async def set_active(request: Request, sound_id: Annotated[str, Form()]):
    active_sound = ActiveSound()
    active_sound.set_active_sound(sound_id)
    return templates.TemplateResponse("views/status.html", {"request": request, "info": f"active sound set to '{sound_id}'"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
