from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce import models as tinymce_models


class Note(models.Model):
    title = models.TextField()
    content = tinymce_models.HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('NoteCategory', on_delete=models.CASCADE, null=True, default=None, blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('notebook_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['id', ]


class NoteCategory(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('notebook_category', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['id', ]
