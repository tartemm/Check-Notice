# Generated by Django 3.1.2 on 2020-10-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20201016_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogovor',
            name='date_end',
            field=models.CharField(max_length=20, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='date_start',
            field=models.CharField(max_length=20, verbose_name='Дата создания'),
        ),
    ]
