from datetime import date, timedelta

import time
from tortoise import Tortoise, run_async
from models import Task


async def init_db():
    await Tortoise.init(
        db_url='sqlite://logistic2.db',
        modules={'models': ['models']})

    await Tortoise.generate_schemas()


quan = 1000


async def create_task():
    start = time.time()
    c = 1
    description1 = ''
    date1 = ''
    invoice1 = ''
    manager1: int
    await Tortoise.init(
        db_url='sqlite://logistic2.db',
        modules={'models': ['models']})

    await Tortoise.generate_schemas()
    for i in range(quan):
        if c == 1:
            payer1 = 'МБК'
            sender1 = 'Медикал Бизнес Комьюнити'
            recipient1 = 'ГБ г. Соликамск'
            urgency1 = 'Срочно'
            manager1 = 3
            c = 2
        elif c == 2:
            payer1 = 'МЕМ'
            sender1 = 'ИП Мандрыгин Е.М.'
            recipient1 = 'Нефтеюганская ОКБ им.Яцкив'
            urgency1 = 'Сверхсрочно'
            manager1 = 4
            c = 3
        elif c == 3:
            payer1 = 'MME'
            sender1 = 'ИП Мандрыгин М.Е.'
            recipient1 = 'ЕВРОМЕДКЛИНИКА ПЛЮС'
            urgency1 = 'Не срочно'
            manager1 = 5
            c = 1
        description1 = f'Коробки {i + 1} мест'
        date1 = date.today() + (-1) ** (i) * timedelta(i)
        invoice1 = f'497-1223478{i}'
        new_tasks = await Task.create(
            date=date1,
            payer=payer1,
            sender=sender1,
            recipient=recipient1,
            description=description1,
            urgency=urgency1,
            invoice=invoice1,
            manager_id=manager1
        )
        await new_tasks.save()
    stop = time.time()

    with open('test_tortoise.txt', 'a', encoding='cp1251') as f:
        f.write(f'Продолжительность добавления {quan} записей составляет {stop - start:.4f} секунд\n')


async def read_task():

    start = time.time()
    await Tortoise.init(
        db_url='sqlite://logistic2.db',
        modules={'models': ['models']})

    await Tortoise.generate_schemas()
    read_tasks = await Task.all()
    for read_task in read_tasks:
        pass
    stop = time.time()

    with open('test_tortoise.txt', 'a', encoding='cp1251') as f:
        f.write(f'Продолжительность чтения {quan} записей составляет {stop - start:.4f} секунд\n')


async def update_task():
    start = time.time()
    await Tortoise.init(
        db_url='sqlite://logistic2.db',
        modules={'models': ['models']})

    await Tortoise.generate_schemas()
    update_tasks = await Task.all()
    for update_task in update_tasks:
        update_task.description = 'Грузовые места 10 шт.'
        update_task.urgency = 'Не срочно'
        await update_task.save()
    stop = time.time()

    with open('test_tortoise.txt', 'a', encoding='cp1251') as f:
        f.write(f'Продолжительность обновления {quan} записей составляет {stop - start:.4f} секунд\n')


async def delete_task():
    start = time.time()
    await Tortoise.init(
        db_url='sqlite://logistic2.db',
        modules={'models': ['models']})

    await Tortoise.generate_schemas()
    await Task.all().delete()
    stop = time.time()
    with open('test_tortoise.txt', 'a', encoding='cp1251') as f:
        f.write(f'Продолжительность удаления {quan} записей составляет {stop - start:.4f} секунд\n')


run_async(create_task())
run_async(read_task())
run_async(update_task())
run_async(delete_task())