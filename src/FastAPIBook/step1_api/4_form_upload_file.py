# -*- coding: utf-8 -*-
# @Project       : FastAPIBook
# @File Name     : 4_form_upload_file.py
# @Author        : liushuangdan 
# @Date          : 2020/7/15 18:32
# @IDE           : PyCharm
from typing import List
from starlette.requests import Request
from fastapi import FastAPI, Form, File, UploadFile
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.post("/file/")
async def files(
                request: Request,
                files_list: List[bytes]             = File(...),
                files_name: List[UploadFile]        = File(...),
            ):
    return templates.TemplateResponse('index.html',
                                      {'request': request,
                                       'file_size': [len(file) for file in files_list],
                                       'filenames': [file.filename for file in files_name],
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
    return templates.TemplateResponse('uploads.html', {'request': request})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
