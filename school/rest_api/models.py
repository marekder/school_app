from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    final_grade = models.IntegerField()


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    points = models.IntegerField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
