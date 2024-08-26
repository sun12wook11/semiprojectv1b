import os
from datetime import datetime
from typing import List
# from weakref import

from fastapi import APIRouter, Request, UploadFile, Form, File
from fastapi.params import Depends, File
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

from app.dbfactory import get_db
from app.schema.gallery import NewGallery
from app.service.GalleryService import get_gallery_data, process_upload

# from app.service.gallery import GalleryService

gallery_router = APIRouter()
templates = Jinja2Templates(directory='views/templates')

# 페이징 알고리즘
# 페이지당 게시글 수 : 25
# 1page : 1 ~ 25
# 2page : 26 ~ 50
# 3page : 51 ~ 75
# ...
# npage : (n-1)*25+1 ~ n*25

# 페이지네이션 알고리즘
# 현재페이지에 따라 보여줄 페이지 블록 결정
# select count(bno) 총게시글수, ceil(count(bno)/25)총페이지수 from board

# ex) 총 페이지수 : 27일때
# cpg = 1: 1 2 3 4 5 6 7 8 9 10
# cpg = 3: 1 2 3 4 5 6 7 8 9 10
# cpg = 9: 1 2 3 4 5 6 7 8 9 10
# cpg = 11: 11 12 13 14 15 16 17 18 19 20
# cpg = 17: 11 12 13 14 15 16 17 18 19 20
# cpg = 23: 21 22 23 24 25 26 27
# stpgb = ((cpg - 1) / 10) * 10 + 1

@gallery_router.get('/list/{cpg}', response_class=HTMLResponse)
async def list(req: Request,cpg: int, db: Session = Depends(get_db)):
    try:

        return templates.TemplateResponse('gallery/list.html',
                                          {'request': req} )

    except Exception as ex:
        print(f'▷▷▷ list 오류 발생 : {str(ex)}')
        return RedirectResponse(url='/member/error', status_code=303)


@gallery_router.get('/write', response_class=HTMLResponse)
async def write(req: Request):
    return templates.TemplateResponse('gallery/write.html', {'request': req})

@gallery_router.post('/write', response_class=HTMLResponse)
async def write(req: Request, gallery: NewGallery = Depends(get_gallery_data), files: List[UploadFile] = File(...)):
    print(gallery)
    attachs = await process_upload(files)
    print(attachs)


    return templates.TemplateResponse('gallery/write.html', {'request': req})


@gallery_router.get('/view', response_class=HTMLResponse)
async def view(req: Request):
    return templates.TemplateResponse('gallery/view.html', {'request': req})