# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
#
# router.register('exams')

from django.urls import path
from .views import ExamView, TaskView
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework.routers import DefaultRouter


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('rest_api.urls'), name='api')
# ]

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

# router = DefaultRouter()

router.register('exams', ExamView, basename='exams').register('tasks', TaskView, basename='exams-tasks',
                                                              parents_query_lookups=['exam'])
router.register('tasks', TaskView)

urlpatterns = router.urls

# urlpatterns = [
#     path("exams/", ExamView.as_view(), name="exams"),
#     path("tasks/", TaskView.as_view(), name="tasks"),
#     # path("exams/<int:id>")
# ]
