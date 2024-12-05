import asyncio
from fastapi import FastAPI
from tortoise import Tortoise
import uvicorn

from db import init_db
import task_r, manager_r

app = FastAPI(title='Логистика Tortoise ORM')

@app.get('/')
async def welcome():
    return {'message': 'Логистика'}




app.include_router(task_r.router)
app.include_router(manager_r.router)

if __name__=='__main__':
    asyncio.run(init_db())