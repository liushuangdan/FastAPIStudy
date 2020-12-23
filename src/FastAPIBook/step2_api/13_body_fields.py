'''
@Author: liushuangdan
@Date: 2020-07-21 17:47:35
@LastEditTime: 2020-07-22 09:17:19
@LastEditors: VScode
@Description: Fields字段验证
@FilePath: \FastAPIBook\step2_api\13_body_fields.py
'''
# -*- coding: utf-8 -*-
from fastapi import FastAPI, Path, Query, Body, Form
from typing import Optional
from pydantic import BaseModel, Field
from starlette.requests import Request

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = Field(None, title="The description of the item.", max_length=6)
    price: float               = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float]       = None

@app.post("/login/")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    print('username', username)
    print('password', password)
    # return {'text_1':text_1 , 'text_2': text_2}
    return {'username': username, 'password': password}

#############################################################

@app.put("/items/")
async def update_item(
    *,
    item_id: int, 
    item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

###############################################################
# example 是body里没有的字段， 不会添加任何验证， 而只会添加字段，不是example 这个字段不行
@app.put("/items-example/")
async def update_item_example(
    *,
    item_id: int, 
    item: Item = Body(..., 
        example = {
            "name": "Foo",
            "description": "A very nice Item",
            "price": 0,
            "tags": 3.2,
        }
        )):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="192.168.62.103", port=8000)