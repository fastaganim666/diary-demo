from django import forms
from .models import *


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass


class DateInput(forms.DateInput):
    input_type = 'date'


class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TaskDay
        fields = ['name', 'date', ]

        widgets = {
            'date': DateInput()
        }


class EditTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = TaskDay
        fields = ['name', 'date', 'tomatoes', 'tomatoes_done', 'is_done']

        widgets = {
            'date': DateInput()
        }
        labels = {
            'name': 'Название',
            'date': 'Дата',
            'tomatoes': 'Томатов запланировано',
            'tomatoes_done': 'Томатов выполнено',
            'is_done': 'Задача выполнена',
        }


class AddTimeForm(forms.ModelForm):
    class Meta:
        model = TimeDay
        fields = ['start', 'end', ]

        widgets = {
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'})
        }

        labels = {
            'start': 'Начало',
            'end': 'Конец',
        }

