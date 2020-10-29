# Generated by Django 3.1.2 on 2020-10-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dogovor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20, verbose_name='Статус')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('date_start', models.DateTimeField(verbose_name='Дата создания')),
                ('date_end', models.DateTimeField(verbose_name='Дата окончания')),
                ('predmet', models.CharField(max_length=100, verbose_name='Предмет')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('agent', models.CharField(max_length=100, verbose_name='Контрагент')),
            ],
            options={
                'verbose_name': 'Договор',
                'verbose_name_plural': 'Договоры',
            },
        ),
        migrations.DeleteModel(
            name='Dogovori',
        ),
    ]