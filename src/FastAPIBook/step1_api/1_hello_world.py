# -*- coding: utf-8 -*-
# @Project       : FastAPIBook
# @File Name     : 1_hello_world.py
# @Author        : liushuangdan 
# @Date          : 2020/7/15 15:20
# @IDE           : PyCharm
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    # 异步标志 async
    return {"message": "Helloworld， FastAPI"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # uvicorn 1_hello_world:app --reload 使用这个命令， 启动项目