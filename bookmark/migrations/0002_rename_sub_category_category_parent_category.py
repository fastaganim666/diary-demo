# Generated by Django 4.1.7 on 2023-03-18 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='sub_category',
            new_name='parent_category',
        ),
    ]
