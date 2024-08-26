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
async def write(req: Request, title: str = Form(...), userid: str = Form(...),
                contents: str = Form(...), files: List[UploadFile] = File(...)):
    print(title, userid, contents)
    print(files)
    UPLOAD_PATH = 'C:/Java/nginx-1.26.2/html/cdn/img/'
    attachs = [] # 업로드된 파일정보를 저장하기 위한 리스트 생성

    today = datetime.today().strftime('%Y%m%d%H%M%S') # UUID 생성
    for file in files:
        if file.filename != '' and file.size > 0:
            nfname = f'{today}{file.filename}'
            # os.path.join(A,B) => A/B (경로생성)
            fname = os.path.join(UPLOAD_PATH, nfname) # 업로드할 파일경로 생성
            content = await file.read() # 업로드할 파일의 내용을 비동기로 읽음
            with open(fname, 'wb') as f:
                f.write(content)
            attach = [nfname, file.size] # 업로드할 파일 정보를 리스트에 저장
            attachs.append(attach)

    print(attachs)


    return templates.TemplateResponse('gallery/write.html', {'request': req})


@gallery_router.get('/view', response_class=HTMLResponse)
async def view(req: Request):
    return templates.TemplateResponse('gallery/view.html', {'request': req})