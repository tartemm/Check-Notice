# Generated by Django 3.1.2 on 2020-10-22 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0015_auto_20201022_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogovor',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Цена'),
        ),
    ]
