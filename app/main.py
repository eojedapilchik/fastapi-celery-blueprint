from fastapi import FastAPI, BackgroundTasks
from app.tasks.divide_task import divide_task
from app.tasks.sum_task import sum_task

app = FastAPI()


# celery = Celery(
#     __name__,
#     broker="redis://127.0.0.1:6379/0",
#     backend="redis://127.0.0.1:6379/0"
# )


@app.get("/")
async def root():
    return {"message": "Welcome -Elad Technologies- API ready to use."}


@app.post("/divide/")
async def divide(a: float, b: float):
    task = divide_task.delay(a, b)
    task_id = task.id
    return {"message": "Divide task is being processed in the background", "task_id": task_id}


@app.post("/suma/")
async def suma(a: float, b: float):
    task = sum_task.delay(a, b)
    task_id = task.id
    return {"message": "Sum task is being processed in the background", "task_id": task_id}
