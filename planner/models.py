from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TaskDay(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    tomatoes = models.IntegerField(null=True, default=None, blank=True)
    tomatoes_done = models.IntegerField(null=True, default=None, blank=True)
    is_done = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['id', ]


class TimeDay(models.Model):
    start = models.TimeField(null=True, default=None, blank=True)
    end = models.TimeField(null=True, default=None, blank=True)
    is_done = models.BooleanField(default=False, blank=True)
    task = models.ForeignKey(TaskDay, on_delete=models.CASCADE, verbose_name='Время', related_name='time')

    def __str__(self):
        return f'{self.start}-{self.end}'

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['id', ]

