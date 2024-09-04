#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def get_task():
    return "НАЧАЛЬНАЯ СТРАНИЦА" 

@app.get("/home")
def get_task():
    return "НЕ НАЧАЛЬНАЯ СТРАНИЦА"     

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

