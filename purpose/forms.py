from django import forms
from .models import *


class CommentForm(forms.Form):
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-input', 'cols': 40, 'rows': 10}))


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateEditPurposeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Название'
        self.fields['deadline'].label = 'Дедлайн'
        self.fields['people'].label = 'Люди'
        self.fields['priority'].label = 'Приоритет (1-5)'
        self.fields['main'].label = 'Главная'

    class Meta:
        model = Purpose
        fields = ['name', 'people', 'deadline', 'priority', 'main', ]

        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 3, 'class': 'bookmark-description'}),
            'deadline': DateInput(),
        }


class CreateStepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = ['name', ]
        widgets = {
            'name': forms.Textarea(attrs={'cols': 60, 'rows': 3, }),
        }

        labels = {
            'name': 'Название',
        }


