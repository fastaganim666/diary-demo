from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Purpose(models.Model):
    name = models.TextField()
    main = models.BooleanField(default=False)
    people = models.TextField(null=True, default=None, blank=True)
    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                   null=True, default=None, blank=True)
    deadline = models.DateField(null=True, default=None, blank=True)
    add_date = models.DateField(auto_now_add=True)
    achieved = models.BooleanField(default=False)
    achievement_date = models.DateField(null=True, default=None, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id', ]

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('purpose_detail', kwargs={'pk': self.pk})


class Step(models.Model):
    name = models.TextField()
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, default=None, blank=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('purpose_detail', kwargs={'pk': self.purpose.pk})

    class Meta:
        ordering = ['id', ]


class Constraint(models.Model):
    name = models.TextField()
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, default=None, blank=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id', ]

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('purpose_detail', kwargs={'pk': self.purpose.pk})

    # def get_absolute_url(self):
    #     return reverse('detail_purpose', kwargs={'pk': self.purpose.pk})


class Skill(models.Model):
    name = models.TextField()
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, default=None, blank=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id', ]

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('purpose_detail', kwargs={'pk': self.purpose.pk})


class Question(models.Model):
    name = models.TextField()
    answer = models.TextField(null=True, default=None, blank=True)
    date_add = models.DateField(auto_now_add=True)
    date_answered = models.DateField(auto_now=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id', ]

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    text = models.TextField()
    add_date = models.DateField(auto_now_add=True)
    edit_date = models.DateField(auto_now=True, null=True, blank=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-add_date', ]

    def __str__(self):
        return f'{self.text}'

    def get_absolute_url(self):
        return reverse('purpose_detail', kwargs={'pk': self.purpose.pk})
