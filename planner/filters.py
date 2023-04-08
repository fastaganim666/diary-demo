from django_filters import FilterSet, DateFilter
from django import forms

from .models import TaskDay


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskFilter(FilterSet):
    date = DateFilter(widget=DateInput(attrs={'type': 'date'}), label='Выберите дату')
    class Meta:
        model = TaskDay
        fields = ['date', ]
