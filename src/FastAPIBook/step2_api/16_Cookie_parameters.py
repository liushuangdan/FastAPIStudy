'''
@Author: liushuangdan
@Date: 2020-07-31 16:02:40
@LastEditTime: 2020-07-31 16:04:06
@LastEditors: VScode
@Description: cookie parameters
@FilePath: \FastAPIBook\step2_api\16_Cookie_parameters.py
'''
# -*- coding: UTF-8 -*-
from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(*, ads_id: str = Cookie(None)):
    return {"ads_id": ads_id}
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)




