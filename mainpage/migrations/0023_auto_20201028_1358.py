# Generated by Django 3.1.2 on 2020-10-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0022_dogovor_docfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogovor',
            name='docfile',
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='status',
            field=models.CharField(choices=[('in_progress', 'Выполняется'), ('done', 'Выполнен')], default='in_progress', max_length=100, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='who',
            field=models.CharField(choices=[('zakazchik', 'Контролировать как заказчик'), ('ispolnitel', 'Контролировать как исполнитель')], default='zakazchik', max_length=100, verbose_name='Сторона контроля'),
        ),
    ]