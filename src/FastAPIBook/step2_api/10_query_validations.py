# -*- coding: utf-8 -*-
'''
@Author: liushuangdan
@Date: 2020-07-20 15:03:18
@LastEditTime: 2020-07-21 11:13:51
@LastEditors: VScode
@Description: 查询参数与字符串验证
@FilePath: \FastAPIBook\step2_api\10_query_validations.py
'''
from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()
###################################################################################
# 限制长度 min_length  max_length
@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3, max_length=50)):
    # 填 None 就是默认值， 填 。。。 则是必填值
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


####################################################################################
# 正则表达式 regex
@app.get("/items2/")
async def read_items2(
        q: str = Query(None, min_length=3, max_length=50, regex="^nice")
    ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


#####################################################################################
# 列表 List
@app.get("/item3/")
async def read_items3(
    q: Optional[List[str]] = Query(["foo", "bar"])
    ):
    query_items = {"q": q}
    return query_items


#####################################################################################
# 别名参数 alias
@app.get("/item4/")
async def read_items4(
    q: Optional[List[str]] = Query(None, alias="item-query")
    ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
        return results


#########################################################
# 弃用参数 deprecated
@app.get("/items5/")
async def read_items5(
    q: str = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
#########################################################



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)