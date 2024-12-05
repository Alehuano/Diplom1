from fastapi import FastAPI
import manager_r
import task_r

app = FastAPI(title='Логистика SQLAlchemy ORM')


@app.get('/')
async def welcome():
    return {'message': 'Логистика'}


app.include_router(manager_r.router)
app.include_router(task_r.router)
