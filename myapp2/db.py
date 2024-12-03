from tortoise import Tortoise

async def init_db():
    await Tortoise.init(
        db_url='sqlite://logistic2.db',
        modules={'models': ['manager_m','task_m']})


    await Tortoise.generate_schemas()
    await Tortoise.close_connections()
    pass