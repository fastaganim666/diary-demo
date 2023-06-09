# Generated by Django 4.1.7 on 2023-03-28 17:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purpose', '0002_remove_step_serial_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-add_date']},
        ),
        migrations.AlterModelOptions(
            name='constraint',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='purpose',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='purpose',
            name='priority',
            field=models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
