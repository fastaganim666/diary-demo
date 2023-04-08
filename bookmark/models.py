from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent_category:
            result = f'{self.parent_category} ({self.name})'
        else:
            result = f'{self.name}'
        return result

    def get_absolute_url(self):
        return reverse('bookmark_category', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['id', ]


class Bookmark(models.Model):
    url = models.URLField()
    description = models.TextField(null=True, default=None, blank=True)
    aliace = models.CharField(max_length=255, null=True, default=None, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.url} - {self.description}'

    def get_absolute_url(self):
        return reverse('bookmark_edit', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['id', ]
