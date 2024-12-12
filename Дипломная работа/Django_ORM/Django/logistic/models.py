from django.db import models


class Manager(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО менеджера')
    department = models.CharField(max_length=100, verbose_name='Подразделение')

    def __str__(self):
        return self.name


class Task(models.Model):
    payer_choice = [
        ('МБК', 'Медикал Бизнес Комьюнити'),
        ('МЕМ', 'ИП Мандрыгин Евгений Михайлович'),
        ('ММЕ', 'ИП Мандрыгин Михаил Ефимович'),
        ('МБКС', 'Медикал Бизнес Комьюнити Сервис'),
        ('СМ', 'Сэплай Мед'),
    ]

    urgency_choice = [
        ('СР', 'Срочно'),
        ('СВХ', 'Сверхсрочно'),
        ('НС', 'Не срочно'),
    ]
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')
    payer = models.CharField(max_length=4,
                             choices=payer_choice,
                             default='МБК',
                             verbose_name='Плательщик')
    sender = models.CharField(max_length=100, verbose_name='Отправитель')
    recipient = models.CharField(max_length=100, verbose_name='Получатель')
    description = models.TextField(verbose_name='Содержание задания')
    urgency = models.CharField(max_length=3,
                               choices=urgency_choice,
                               default='СР',
                               verbose_name='Срочность')
    invoice = models.CharField(max_length=15, verbose_name='Номер накладной')
    manager = models.ForeignKey(Manager, on_delete=models.PROTECT, verbose_name='Менеджер')

    def __str__(self):
        return f'{self.payer},{self.sender},{self.recipient}'
# Create your models here.
