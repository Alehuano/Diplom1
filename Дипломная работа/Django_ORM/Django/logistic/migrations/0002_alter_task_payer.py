# Generated by Django 4.2.16 on 2024-12-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='payer',
            field=models.CharField(choices=[('МБК', 'Медикал Бизнес Комьюнити'), ('МЕМ', 'ИП Мандрыгин Евгений Михайлович'), ('ММЕ', 'ИП Мандрыгин Михаил Ефимович'), ('МБКС', 'Медикал Бизнес Комьюнити Сервис'), ('СМ', 'Сэплай Мед')], default='МБК', max_length=4, verbose_name='Плательщик'),
        ),
    ]
