from schemas import Tasks
from fastapi import APIRouter
from tasks import crud

router = APIRouter(prefix="/tasks")

@router.get("/getTask")
def getAll():
    pass

@router.post("/createTask")
def createTask(task: Tasks):
    return crud.createTask(task)