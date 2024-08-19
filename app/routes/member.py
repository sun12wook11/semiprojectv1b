from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

member_router = APIRouter()
templates = Jinja2Templates(directory='views/templates')

@member_router.get("/join", response_class=HTMLResponse)
async def join(request: Request):
    return templates.TemplateResponse("member/join.html", {"request": request})

@member_router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("member/login.html", {"request": request})

@member_router.get("/myinfo", response_class=HTMLResponse)
async def myinfo(request: Request):
    return templates.TemplateResponse("member/myinfo.html", {"request": request})