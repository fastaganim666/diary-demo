from django import forms
from tinymce.widgets import TinyMCE
from .models import *


# class AddNoteForms(forms.ModelForm):
#     content = forms.CharField(widget=TinyMCE())

class AddNoteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = NoteCategory.objects.filter(user_id=user)

    content = forms.CharField(widget=TinyMCE(), label='')
    class Meta:
        model = Note
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(),
        }
        labels = {
            'title': 'Название',
            'category': 'Категория',
        }


class AddNoteCategory(forms.ModelForm):
    class Meta:
        model = NoteCategory
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(),
        }
        labels = {
            'name': 'Название',
        }
