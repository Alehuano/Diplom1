from tortoise.models import Model
from tortoise.fields import CharField, IntField


class Manager(Model):
    id = IntField(pk=True)
    name = CharField(max_length=10)
    department = CharField(max_length=100)

    class Meta:
        table = 'manager'

    def __str__(self):
        return self.name