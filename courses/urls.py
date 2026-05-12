from django.urls import path

from courses.views import CourseListCreateView

urlpatterns = [
    path('', CourseListCreateView.as_view(), name='courses'),
]