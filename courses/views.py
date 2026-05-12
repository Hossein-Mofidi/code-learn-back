from rest_framework import generics

from courses.models import Course

from courses.permissions import IsInstructor
from courses.serializers import CourseSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsInstructor]

    def get_queryset(self):
        return Course.objects.filter(instructor__id=self.request.user.id)