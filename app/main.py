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


# @celery.task
# def divide(x, y):
#     import time
#     time.sleep(5)
#     return x / y


@app.post("/divide/")
async def divide(a: float, b: float, background_tasks: BackgroundTasks):
    background_tasks.add_task(divide_task, a, b)
    return {"message": "Task scheduled"}


@app.post("/suma/")
async def suma(a: float, b: float, background_tasks: BackgroundTasks):
    background_tasks.add_task(sum_task, a, b)
    return {"message": "Task scheduled"}
