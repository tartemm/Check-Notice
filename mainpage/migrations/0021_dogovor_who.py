# Generated by Django 3.1.2 on 2020-10-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0020_auto_20201023_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogovor',
            name='who',
            field=models.CharField(choices=[('zakazchik', 'Контролировать как заказчик'), ('ispolnitel', 'Контролировать как исполнитель')], default='zakazchik', max_length=100, verbose_name='Тип договора'),
        ),
    ]