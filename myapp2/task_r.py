from fastapi import APIRouter, status, HTTPException
from tortoise import Tortoise

from db import init_db
from manager_m import Manager
from task_m import Task
from schemas import CreateTask, UpdateTask

router = APIRouter(prefix="/task", tags=["Задачи"])


@router.get("/all_tasks")
async def get_all_tasks():
    await init_db()
    tasks = await Task.all()
    await Tortoise.close_connections()
    return tasks


@router.post("/create")
async def create_task(create_task: CreateTask, manager_id: int):
    await init_db()
    await Task.create(date=create_task.date,
                      payer=create_task.payer,
                      sender=create_task.sender,
                      recipient=create_task.recipient,
                      description=create_task.description,
                      urgency=create_task.urgency,
                      invoice=create_task.invoice,
                      manager_id=manager_id)

    await Tortoise.close_connections()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Задача успешно добавлена'}


@router.put("/update")
async def update_task(task_id: int, update_task: UpdateTask):
    await init_db()
    task = await Task.get(task_id=task_id)
    update_task = {
        'payer': update_task.payer,
        'sender': update_task.sender,
        'recipient': update_task.recipient,
        'description': update_task.description,
        'urgency': update_task.urgency,
        'invoice': update_task.invoice
    }
    await task.update_from_dict(update_task)
    await task.save()
    await Tortoise.close_connections()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Задача успешно обновлена'}


@router.delete("/delete")
async def delete_task(task_id: int):
    await init_db()
    task = await Task.get(task_id=task_id)
    await task.delete()
    await Tortoise.close_connections()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Задача успешно удалена'}
