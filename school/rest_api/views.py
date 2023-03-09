from django.shortcuts import render
from .models import Exam, Task
from .serializers import ExamSerializer, TaskSerializer
from rest_framework.viewsets import ModelViewSet


# from rest_framework.generics import ListCreateAPIView


class ExamView(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# class ExamView(ListCreateAPIView):
#     queryset = Exam.objects.all()
#     serializer_class = ExamSerializer
#
#
# class TaskView(ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
