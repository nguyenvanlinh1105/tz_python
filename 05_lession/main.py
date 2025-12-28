from fastapi import FastAPI
from app.core.config import settings
from app.core.middleware import TraceIdMiddleware
from app.api import todo_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(TraceIdMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_router.router)

@app.get("/")
def root():
    return {"msg": "Todo API is running!"}

