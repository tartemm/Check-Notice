# Generated by Django 3.1.2 on 2020-10-22 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0017_dogovor_tip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogovor',
            name='tip',
        ),
    ]
