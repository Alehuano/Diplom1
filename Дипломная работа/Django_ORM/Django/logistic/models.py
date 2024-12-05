from django.db import models


class Manager(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО менеджера')
    department = models.CharField(max_length=100, verbose_name='Подразделение')

    def __str__(self):
        return self.name


class Task(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')
    payer = models.CharField(max_length=10, verbose_name='Плательщик')
    sender = models.CharField(max_length=100, verbose_name='Отправитель')
    recipient = models.CharField(max_length=100, verbose_name='Получатель')
    description = models.TextField(verbose_name='Содержание задания')
    urgency = models.CharField(max_length=10, verbose_name='Срочность')
    invoice = models.CharField(max_length=15, verbose_name='Номер накладной')
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT, verbose_name='Менеджер')

    def __str__(self):
        return f'{self.payer},{self.sender},{self.recipient}'
# Create your models here.
