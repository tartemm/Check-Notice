from .models import Dogovor
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput, Select


class DogovorForm(ModelForm):
    class Meta:
        model = Dogovor
        fields = ["who", "type", "status", "name", "predmet", "price", "agent", "date_start", "date_end"]
        widgets = {
            "who": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Сторона контроля'
            }),
            "type": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Тип договора'
            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус договора'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
            "predmet": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Предмет'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена, руб.'
            }),
            "agent": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Контрагент'
            }),
            "date_start": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата создания, дд.мм.гггг'
            }),
            "date_end": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания, дд.мм.гггг'
            })
        }


    # def __init__(self, arg):
    #     super(DogovorForm, self).__init__()
    #     self.arg = arg
