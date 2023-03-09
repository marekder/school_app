# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
#
# router.register('exams')

from django.urls import path
from .views import ExamView, TaskView

from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('rest_api.urls'), name='api')
# ]

router = DefaultRouter()

router.register('exams', ExamView)
router.register('tasks', TaskView)

urlpatterns = router.urls

# urlpatterns = [
#     path("exams/", ExamView.as_view(), name="exams"),
#     path("tasks/", TaskView.as_view(), name="tasks"),
#     # path("exams/<int:id>")
# ]
