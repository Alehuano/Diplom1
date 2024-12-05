from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from typing import Annotated

from manager_m import Manager
from task_m import Task
from schemas import CreateTask, UpdateTask
from db_depends import get_db

router = APIRouter(prefix='/task', tags=['Задача'])


@router.get('/all_task')
async def get_all_task(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, manager_id: int):
    manager = db.scalars(select(Manager).where(Manager.id == manager_id))
    if manager is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Менеджер не найден')
    db.execute(insert(Task).values(date=create_task.date,
                                   payer=create_task.payer,
                                   sender=create_task.sender,
                                   recipient=create_task.recipient,
                                   description=create_task.description,
                                   urgency=create_task.urgency,
                                   invoice=create_task.invoice,
                                   manager_id=manager_id))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Задача успешно добавлена'}


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], update_task: UpdateTask, task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Задача не найдена')
    db.execute(update(Task).values(payer=update_task.payer,
                                   sender=update_task.sender,
                                   recipient=update_task.recipient,
                                   description=update_task.description,
                                   urgency=update_task.urgency,
                                   invoice=update_task.invoice))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Задача успешно обновлена'}


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Задача не найдена')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Задача успешно удалена'}
