# Generated by Django 3.1.13 on 2023-08-28 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20230828_0806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam_model',
            old_name='student_group',
            new_name='section',
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 28, 21, 57, 10, 262363)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 28, 21, 57, 10, 262363)),
        ),
    ]