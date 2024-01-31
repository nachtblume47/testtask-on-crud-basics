

from fastapi import FastAPI
from src.manager.router import manager_router
import uvicorn

app = FastAPI(
    title="CRUD test task",
    version="0.0.1"
)
app.include_router(manager_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)