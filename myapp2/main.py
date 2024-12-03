from fastapi import FastAPI
from tortoise import Tortoise
import uvicorn

from db import init_db
import task_r, manager_r

app = FastAPI(title='Логистика')

@app.get('/')
async def welcome():
    return {'message': 'Логистика'}




app.include_router(task_r.router)
app.include_router(manager_r.router)
