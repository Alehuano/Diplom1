from fastapi import APIRouter, status, HTTPException
from tortoise import Tortoise

from db import init_db
from manager_m import Manager
from task_m import Task
from schemas import CreateManager, UpdateManager

router = APIRouter(prefix="/manager", tags=["Менеджер"])


@router.get("/all_managers")
async def get_all_managers():
    await init_db()
    managers = await Manager.all()
    await Tortoise.close_connections()
    return managers


@router.post("/create")
async def create_manager(create_manager: CreateManager):
    await init_db()
    await Manager.create(name=create_manager.name,
                         department=create_manager.department)
    await Tortoise.close_connections()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Менеджер успешно добавлен'}


@router.put("/update")
async def update_manager(manager_id: int, update_manager: UpdateManager):
    await init_db()
    manager = await Manager.get(manager_id=manager_id)
    update_manager = {
        'name': update_manager.name,
        'department': update_manager.department
    }
    await manager.update_from_dict(update_manager)
    await manager.save()
    await Tortoise.close_connections()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Менеджер успешно обновлен'}


@router.delete("/delete")
async def delete_manager(manager_id: int):
    await init_db()
    manager = await Manager.get(manager_id=manager_id)
    await manager.delete()
    await Tortoise.close_connections()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Менеджер успешно удален'}
