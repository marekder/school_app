# Generated by Django 4.1.7 on 2023-03-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_rename_exams_task_exam_alter_task_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='points',
            field=models.IntegerField(),
        ),
    ]