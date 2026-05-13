from rest_framework import generics, viewsets

from courses.models import Course, Category
from courses.openapi import category_list_schema, course_viewset_schema

from courses.permissions import IsVerifiedInstructor
from courses.serializers import CourseSerializer, CategorySerializer


@category_list_schema
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@course_viewset_schema
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [IsVerifiedInstructor]

    def get_queryset(self):
        return Course.objects.filter(instructor=self.request.user)