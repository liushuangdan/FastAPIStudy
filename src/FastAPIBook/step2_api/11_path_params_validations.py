'''
@Author: liushuangdan
@Date: 2020-07-20 18:14:56
@LastEditTime: 2020-07-21 14:02:06
@LastEditors: VScode
@Description: 路径参数与数值验证
@FilePath: \FastAPIBook\step2_api\11_path_params_validations.py
'''
# -*- coding: utf-8 -*-
from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    # ge 大于等于 gt 大于 le 小于等于 lt 小于
    # gt：大于（greater than）
    # ge：大于等于（greater than or equal）
    # lt：小于（less than）
    # le：小于等于（less than or equal）
    item_id: int = Path(..., title="The ID of the item of get", ge=50, le=100),
    q: Optional[str] = Query(None, alias="item-query"),
    size: float = Query(1, gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)