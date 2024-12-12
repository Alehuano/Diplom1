import time
from db import session
from task_m import Task
from datetime import date, timedelta

quan = 1000


def create_task():
    start = time.time()
    c = 1
    description1 = ''
    date1 = ''
    invoice1 = ''
    manager1 = ''

    for i in range(quan):
        if c == 1:
            payer1 = 'МБК'
            sender1 = 'Медикал Бизнес Комьюнити'
            recipient1 = 'ГБ г. Соликамск'
            urgency1 = 'Срочно'
            manager1 = 4
            c = 2
        elif c == 2:
            payer1 = 'МЕМ'
            sender1 = 'ИП Мандрыгин Е.М.'
            recipient1 = 'Нефтеюганская ОКБ им.Яцкив'
            urgency1 = 'Сверхсрочно'
            manager1 = 2
            c = 3
        elif c == 3:
            payer1 = 'MME'
            sender1 = 'ИП Мандрыгин М.Е.'
            recipient1 = 'ЕВРОМЕДКЛИНИКА ПЛЮС'
            urgency1 = 'Не срочно'
            manager1 = 3
            c = 1
        description1 = f'Коробки {i + 1} мест'
        date1 = date.today() + (-1) ** (i) * timedelta(i)
        invoice1 = f'497-1223478{i}'
        new_tasks = Task(
            date=date1,
            payer=payer1,
            sender=sender1,
            recipient=recipient1,
            description=description1,
            urgency=urgency1,
            invoice=invoice1,
            manager_id=manager1
        )
        session.add(new_tasks)
    session.commit()
    stop = time.time()

    with open('test_sqlalchemy.txt', 'a', encoding='cp1251') as f:
        f.write(f'Продолжительность добавления {quan} записей составляет {stop - start:.4f} секунд\n')


def read_task():
    start = time.time()
    read_tasks = session.query(Task).all()
    for read_task in read_tasks:
        pass
    stop = time.time()

    with open('test_sqlalchemy.txt', 'a', encoding='cp1251') as f:
        f.write(f'Продолжительность чтения {quan} записей составляет {stop - start:.4f} секунд\n')


def update_task():
    start = time.time()
    update_tasks = session.query(Task).all()
    for update_task in update_tasks:
        update_task.description = f'Грузовые места 10 шт.'
        update_task.urgency = 'Не срочно'
        session.add(update_task)
    session.commit()
    stop = time.time()

    with open('test_sqlalchemy.txt', 'a', encoding='cp1251') as f:
        f.write(f'Продолжительность обновления {quan} записей составляет {stop - start:.4f} секунд\n')


def delete_task():
    start = time.time()
    session.query(Task).delete()
    session.commit()
    stop = time.time()
    with open('test_sqlalchemy.txt', 'a', encoding='cp1251') as f:
        f.write(f'Продолжительность удаления {quan} записей составляет {stop - start:.4f} секунд\n')

create_task()
read_task()
update_task()
delete_task()
