from django.db import models

# Create your models here.
class Dogovor(models.Model):
    TYPE_CHOICES = [
        ('postavka', 'Договор поставки'),
        ('uslugi', 'Договор оказания юридических услуг'),
        ('perevoz', 'Договор перевозки груза автомобильным транспортом'),
        ('stroitelny', 'Договор строительного подряда')
    ]
    WHO_CHOICES = [
        ('zakazchik', 'Контролировать как заказчик'),
        ('ispolnitel', 'Контролировать как исполнитель')
    ]
    STATUS_CHOICES = [
        ('in_progress', 'Выполняется'),
        ('done', 'Выполнен')
    ]
    status = models.CharField(
        max_length=100,
        verbose_name='Статус',
        choices=STATUS_CHOICES,
        default='in_progress'
    )
    name = models.CharField('Наименование', max_length = 100)
    date_start = models.DateField('Дата создания')
    date_end = models.DateField('Дата окончания')
    predmet = models.CharField('Предмет', max_length = 100)
    price = models.DecimalField('Цена', max_digits = 9, decimal_places = 0)
    agent = models.CharField('Контрагент', max_length = 100)
    type = models.CharField(
        max_length=100,
        verbose_name='Тип договора',
        choices=TYPE_CHOICES,
        default='postavka'
    )
    who = models.CharField(
        max_length=100,
        verbose_name='Сторона контроля',
        choices=WHO_CHOICES,
        default='zakazchik'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class KT(models.Model):
    dogovor = models.ForeignKey(Dogovor, on_delete = models.CASCADE)
    kt_name = models.CharField('Название этапа', max_length = 100)
    kt_status = models.CharField('Статус этапа', max_length = 20)
    kt_start = models.DateField('Дата начала')
    kt_end = models.DateField('Дата окончания')
    prosrochka = models.PositiveIntegerField('Просрочка', default = 0)

    def __str__(self):
        return self.kt_name

    class Meta:
        verbose_name = 'Контрольная точка'
        verbose_name_plural = 'Контрольные точки'


class Comment(models.Model):
    dogovor_number = models.ForeignKey(Dogovor, on_delete = models.CASCADE)
    author = models.CharField('Имя комментатора', max_length = 50)
    comment_text = models.CharField('Текст комментария', max_length = 500)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
