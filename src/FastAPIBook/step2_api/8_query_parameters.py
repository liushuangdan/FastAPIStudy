'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑       永不宕机     永无BUG
'''
# -*- coding: utf-8 -*-
# @Project       : FastAPIBook
# @File Name     : 8_query_parameters.py
# @Author        : liushuangdan 
# @Date          : 2020/7/17 16:16
# @IDE           : PyCharm
from fastapi import FastAPI


app = FastAPI()
fake_item_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    '''
    @description: 
    @param {type} 
    @return: 
    '''    
    return fake_item_db[skip : skip + limit]


@app.get("/i/")
async def i(A: str = "HI...", B: str = "Hello, jack", C: str = "He.."):
    return {"cc": A+B+C}, {"dd": B+C}


@app.get("ii")
async def ii(A: int = 0, B: int = 10, C: int = 20):
    return {"cc": A+B+C}, {"dd": B+C}


@app.get("iii")
async def iii(A: int = 0, B: int = 10, C: int = 20):
    return "A+B+C", A+B+C


# bool 类型强制转换
@app.get("/xxx/{item_id}")
async def xxx(item_id: str, QQ: str = None, SS: bool = False):
    '''
    @description: 
    @param {type}:
        QQ 为 选填参数。
        item_id 为必填参数。
        SS： 为选填参数。 
    @return: 
    '''
    item = {"item_id": item_id}
    if QQ:
        item.update(
            {"QQ": QQ}
        )
    if not SS:
        item.update(
            {"item_id": "This is SSSSSSS(n个s)"}
        )
    return item


# 多路径 和 查询参数 和 必填字段
@app.get("/user/{user_id}/item/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update(
            {"q": q}
        )
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item 


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

