from fastapi import FastAPI
from controller.todo_controller import router as todo_router

app = FastAPI()

app.include_router(todo_router)
