from database import Tasks, new_session

def createTask(task: Tasks) -> bool:
    with new_session() as session:
        task_dict = task.model_dump()

        task = Tasks(**task_dict)
        session.add(task)
        session.flush()
        session.commit()
        return True
    

