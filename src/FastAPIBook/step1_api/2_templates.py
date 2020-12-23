# -*- coding: utf-8 -*-
# @Project       : FastAPIBook
# @File Name     : 2_templates.py
# @Author        : liushuangdan 
# @Date          : 2020/7/15 15:45
# @IDE           : PyCharm
from starlette.requests import Request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def main(request: Request):
    request = request
    hello = 'hello_word'
    return templates.TemplateResponse("index.html", locals())


@app.get("/{item_id}/")
async def item_id(request: Request, item_id):
    item_id = item_id
    return templates.TemplateResponse('index.html', locals())


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)