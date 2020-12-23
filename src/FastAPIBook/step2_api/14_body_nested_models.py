'''
@Author: liushuangdan
@Date: 2020-07-22 09:20:18
@LastEditTime: 2020-07-22 12:03:39
@LastEditors: VScode
@Description: body nested models 嵌套模型
@FilePath: \FastAPIBook\step2_api\14_body_nested_models.py
'''
# -*- coding: utf-8 -*-
from fastapi import FastAPI, Path, Query, Body, Form
from typing import Optional, List, Set, Dict
from pydantic import BaseModel, Field, HttpUrl
from starlette.requests import Request


app = FastAPI()

# class Item(BaseModel):
#     name = str
#     description: str = None
#     price: float
#     tax: float       = None
#     tags0: list      = []
#     tags1: List[str] = []
#     tags2: Set[str]  = set()


# class Image(BaseModel):
#     url: str
#     name: str

class Items(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = set() # 集合 创建一个空集合必须用 set() 而不是 {}
    image: Image = None # 试用子模型作为类型
    images: List[Image] = None # 带有子模型列表的属性


# @app.put("/items/{item_id}")
# async def update_item(*, item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

class Image(BaseModel):
    url: HttpUrl    # 该字符串将被检查为有效的URL，并在JSON Schema / OpenAPI中进行记录。
                    # 特殊类型和验证 https://pydantic-docs.helpmanual.io/usage/types/
    name: str

# 纯列表体
@app.post("/images/multiple/")
async def create_multiple_images(*, images: List[Image]):
    return images

# 任意dicts (无需事先知道有效的字段/属性名称是什么)(如果您想接收未知的密钥，这将很有用。)
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]): 
    return weights
    

@app.put("/items-image/{item_id}")
async def update_item_image(*, item_id: int, items: Items):
    results = {"item_id": item_id, "items": items}
    return results


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)