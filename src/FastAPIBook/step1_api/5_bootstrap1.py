# -*- coding: utf-8 -*-
# @Project       : FastAPIBook
# @File Name     : 5_bootstrap1.py
# @Author        : liushuangdan 
# @Date          : 2020/7/16 16:35
# @IDE           : PyCharm
from starlette.requests import Request
from fastapi import FastAPI, Form, File, UploadFile
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.post("/user/")
async def user(
                request: Request,
                username: str = Form(...),
                password: str = Form(...),
            ):
    print("username: ", username)
    print("password: ", password)
    return templates.TemplateResponse('index_bootstrap.html',
                                      {'request': request,
                                       'username': username,
                                       })


@app.post("/create_file/")
async def create_file(
                    request: Request,
                    file: bytes          = File(...),
                    fileb: UploadFile    = File(...),
                    notes: str           = Form(...),
            ):
    return templates.TemplateResponse('index.html',
                                      {'request': request,
                                       'file_size': len(file),
                                       'notes': notes,
                                       "fileb_content_type": fileb.content_type
                                       })


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('signin.html', {'request': request})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # 基础篇 感性认识Fast API
    # 1. 高性能，异步并发，高效开发，稳定，简单易用。
