# Generated by Django 3.1.2 on 2020-10-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0019_dogovor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogovor',
            name='type',
            field=models.CharField(choices=[('postavka', 'Договор поставки'), ('uslugi', 'Договор оказания юридических услуг'), ('perevoz', 'Договор перевозки груза автомобильным транспортом'), ('stroitelny', 'Договор строительного подряда')], default='postavka', max_length=100, verbose_name='Тип договора'),
        ),
    ]
