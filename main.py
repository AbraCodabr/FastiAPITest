#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# @app.get("/home")
# def get_task():
#     return {"details": "НЕ НАЧАЛЬНАЯ СТРАНИЦА"}     

#по умолчанию открывает фаил индекс 
app.mount("/", StaticFiles(directory="static", html=True))

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

