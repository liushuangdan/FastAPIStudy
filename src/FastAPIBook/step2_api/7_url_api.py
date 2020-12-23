# -*- coding: utf-8 -*-
# @Project       : FastAPIBook
# @File Name     : 7_url_api.py
# @Author        : liushuangdan 
# @Date          : 2020/7/17 15:13
# @IDE           : PyCharm
from fastapi import FastAPI
from enum import Enum


class Name(str, Enum):
    Jack = "任中"
    Diana = "刘双丹"
    Bob = "温宁"

app = FastAPI()


@app.get("/{who}")
async def get_day(who: Name):
    if who == Name.Jack:
        return {"who": who, "message": "任中是个大坏蛋~"}
    elif who == Name.Bob:
        return {"who": who, "message": "世人唤我鬼将军，唯你唤我温琼林！"}
    return {"who": who, "message": "刘双丹在学习Fastapi~"}


@app.get("/")
async def main():
    return {"message": "Hello, FastAPI~"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)