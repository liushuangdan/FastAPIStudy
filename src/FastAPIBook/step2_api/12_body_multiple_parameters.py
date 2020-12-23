'''
@Author: liushuangdan
@Date: 2020-07-21 13:56:30
@LastEditTime: 2020-07-21 17:23:18
@LastEditors: VScode
@Description: 主体多个参数
@FilePath: \FastAPIBook\step2_api\12_body_multiple_parameters.py
'''
# -*- coding: utf-8 -*-
from fastapi import FastAPI, Path, Query, Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


###################################################################
# 混合参数
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000), 
    q: str = None,
    item: Item = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


###################################################################
# body 的奇异值
@app.put("/items-mix/{item_id}")
async def update_item_strange(
    item_id: int, item: Item, user: User, importance: int = Body(...)
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

######################################################################
# 传入一个单body的参数 embed 嵌入 True
"""
{
  "item": {
    "name": "string",
    "description": "string",
    "price": 0,
    "tax": 0
  }
}
"""
# 传入一个单body的参数 embed 嵌入 False
"""
{
  "name": "string",
  "description": "string",
  "price": 0,
  "tax": 0
}
"""
@app.put("/items-single/{item_id}")
async def update_items_single(
    *,
    item_id: int, 
    item: Item = Body(..., embed=False)
):
    results = {"item_id": item_id}
    return results


##################################################################
# 多主体参数和查询
@app.put("/items-multiple/{item_id}")
async def update_items_multiple(
    *,
    item_id: int, 
    item: Item,
    user: User,
    importance: int = Body(..., gt=0),
    q: str = None
):
    results = {"item_id": item_id, "item": Item, "user": User, "importance": importance}
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)