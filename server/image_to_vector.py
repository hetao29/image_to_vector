# -*- coding: utf-8 -*-
# @file   : reverse_image_search_main.py
# @author : songxulin
# @date   : 2022:10:16 11:00:00
# @version: 1.0
# @desc   : 程序主入口
import os
import json
from typing import Optional, List, Optional, Any

import uvicorn
from encode import Resnet50
from fastapi import FastAPI
from logs import LOGGER
from operations.convert import do_convert
from pydantic import BaseModel, Json
from starlette.middleware.cors import CORSMiddleware
from util import image_util
from fastapi import Response

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
MODEL = Resnet50()

class UploadImagesModel(BaseModel):
    image: Optional[str] = ""
    url: Optional[str] = ""

@app.post('/convert')
async def upload_images(imagesModel: UploadImagesModel):
    try:
        # Save the upload image to server.
        img_path = image_util.down_image(imagesModel.image, imagesModel.url)

        vector = do_convert(imagesModel, img_path, MODEL)
        d={'code': 10000, 'message': 'Successfully', 'data': vector}
        json_str = json.dumps(d, indent=4, default=str)
        return Response(content=json_str, media_type='application/json')
    except Exception as e:
        LOGGER.error(e)
        return {'code': 10100, 'message': str(e)}

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=5002)
