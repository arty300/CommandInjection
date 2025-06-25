from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.utils import run_ping_command

app = FastAPI(title="CTF Command Injection Challenge")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    return FileResponse(path="static/index.html")

@app.post("/ping", response_class=HTMLResponse)
async def ping_host(host: str = Form(...)):
    try:
        result = run_ping_command(host)
        return result
    except ValueError as e:
        return str(e)