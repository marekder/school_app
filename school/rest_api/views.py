from django.shortcuts import render
from .models import Exam, Task
from .serializers import ExamSerializer, TaskSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsExamOwnerOrReadOnly, IsOwnerOrReadOnly
from rest_framework import permissions


# from rest_framework.generics import ListCreateAPIView


class ExamView(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsExamOwnerOrReadOnly)

# class ExamView(ListCreateAPIView):
#     queryset = Exam.objects.all()
#     serializer_class = ExamSerializer
#
#
# class TaskView(ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
