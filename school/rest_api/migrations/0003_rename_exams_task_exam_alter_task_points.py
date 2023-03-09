# Generated by Django 4.1.7 on 2023-03-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_rename_exam_task_exams'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='exams',
            new_name='exam',
        ),
        migrations.AlterField(
            model_name='task',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
