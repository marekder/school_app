# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
#
# router.register('exams')

from django.urls import path
from .views import ExamView, TaskView

urlpatterns = [
    path("exams/", ExamView.as_view(), name="exams"),
    path("tasks/", TaskView.as_view(), name="tasks"),
    # path("exams/<int:id>")
]
