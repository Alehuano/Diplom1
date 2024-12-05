from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from typing import Annotated

from manager_m import Manager
from task_m import Task
from schemas import CreateManager, UpdateManager
from db_depends import get_db

router = APIRouter(prefix='/manager', tags=['Менеджер'])


@router.get('/all_managers')
async def get_all_managers(db: Annotated[Session, Depends(get_db)]):
    managers = db.scalars(select(Manager)).all()
    return managers


@router.post('/create')
async def create_manager(db: Annotated[Session, Depends(get_db)], create_manager: CreateManager):
    db.execute(insert(Manager).values(name=create_manager.name,
                                      department=create_manager.department))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Менеджер успешно добавлен'}


@router.put('/update')
async def update_manager(db: Annotated[Session, Depends(get_db)],
                         manager_id: Annotated[int, Query(...)],
                         update_manager: UpdateManager):
    manager = db.scalar(select(Manager).where(Manager.id == manager_id))
    if manager is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Менеджер не найден'
        )
    db.execute(update(Manager).where(Manager.id == manager_id).values(name=update_manager.name,
                                                                      department=update_manager.department))

    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Менеджер успешно обновлен'}


@router.delete('/delete')
async def delete_manager(db: Annotated[Session, Depends(get_db)],
                         manager_id: Annotated[int, Query(...)]):
    manager = db.scalar(select(Manager).where(Manager.id == manager_id))
    if manager is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Менеджер не найден'
        )
    db.execute(delete(Manager).where(Manager.id == manager_id))
    # db.execute(delete(Task).where(Task.manager_id == manager_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Менеджер успешно удален'}
