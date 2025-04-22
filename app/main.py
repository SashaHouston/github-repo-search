from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from app.routes.search_router import router
import logging

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

logging.basicConfig(level=logging.INFO)

app.include_router(router, prefix="/api")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def show_homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
