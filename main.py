
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from database import create_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")  
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def get_task(request: Request):
    return templates.TemplateResponse(name='index.html', context={'request': request})   

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)