'''
@Author: liushuangdan
@Date: 2020-07-22 12:04:05
@LastEditTime: 2020-07-31 16:00:10
@LastEditors: VScode
@Description: 额外的数据类型
@FilePath: \FastAPIBook\step2_api\15_extra_data_types.py
'''
# -*- coding: UTF-8 -*-
from datetime import datetime, time, timedelta
from uuid import UUID
from uuid import uuid1
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

# class Item(BaseModel):
#     xxx: UUID
#     ...
class Item(BaseModel):
    start_datetime: datetime
    end_datetime: datetime
    repeat_at: time 
    process_after: timedelta 
    start_process: str 
    duration: str 

# 额外数据类型
# https://fastapi.tiangolo.com/tutorial/extra-data-types/
@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID ,
    start_datetime: datetime = Body(None),
    end_datetime: datetime = Body(None),
    repeat_at: time = Body(None),
    process_after: timedelta = Body(None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


# 额外数据类型
# https://fastapi.tiangolo.com/tutorial/extra-data-types/
@app.put("/items2/{item_id}")
async def read_items2(item_id: UUID, item: Item):
    item.start_process = item.start_datetime + item.process_after
    item.duration = item.end_datetime - item.start_process
    return {"item_id": item_id, 'item':item }

    

if __name__ == '__main__':
    import uvicorn
    print('uuid:', uuid1())
    uvicorn.run(app, host="127.0.0.1", port=8000)  