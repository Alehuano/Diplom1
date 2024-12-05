from tortoise.models import Model
from tortoise.fields import CharField, IntField, DatetimeField, ForeignKeyField


class Manager(Model):
    id = IntField(pk=True)
    name = CharField(max_length=50)
    department = CharField(max_length=100)

    class Meta:
        table = 'manager'

    def __str__(self):
        return self.name


class Task(Model):
    id = IntField(pk=True)
    payer = CharField(max_length=20)
    sender = CharField(max_length=255)
    recipient = CharField(max_length=255)
    description = CharField(max_length=500)
    date = CharField(max_length=10)
    urgency = CharField(max_length=20)
    invoice = CharField(max_length=30)
    manager = ForeignKeyField('models.Manager', related_name='tasks')

    class Meta:
        table = 'task'

    def __str__(self):
        return f'{self.payer}{self.sender}{self.recipient}'