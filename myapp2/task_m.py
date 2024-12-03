from tortoise.models import Model
from tortoise.fields import CharField, IntField, DatetimeField, ForeignKeyField
from manager_m import Manager


class Task(Model):
    id = IntField(pk=True)
    payer = CharField(max_length=20)
    sender = CharField(max_length=255)
    recipient = CharField(max_length=255)
    description = CharField(max_length=500)
    date = DatetimeField()
    urgency = CharField(max_length=20)
    invoice = CharField(max_length=30)
    manager = ForeignKeyField('manager_m.Manager', related_name='tasks')

    class Meta:
        table = 'task'

    def __str__(self):
        return f'{self.payer}{self.sender}{self.recipient}'
