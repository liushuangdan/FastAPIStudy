# -*- coding: utf-8 -*-
# @Project       : FastAPIBook
# @File Name     : 6_url_api.py
# @Author        : liushuangdan 
# @Date          : 2020/7/17 9:35
# @IDE           : PyCharm
from fastapi import FastAPI

app = FastAPI()


@app.get("/me/xx")
async def read_item_me():
    return {"me":  'me'}


@app.get("/me/{item_id}")
async def read_item(item_id: str):
    # 这里直接接收int类型会报错， 如果需要int类型的参数转换一个
    return {"item_id": item_id}


# 同一个名字开头的url，固定的url配置放在关键字参数接收的url前面
# 放在后面，url请求会直接进入到关键字参数接收的函数中。
# @app.get("/me/xx")
# async def read_item_me():
#     return {"me":  'me'}


@app.get("/")
async def main():
    return {"message": "Hello, FastAPI~"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
