from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.serializers import ProfileSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return get_user_model().objects.filter(id=user.id)

    def get_object(self):
        return self.request.user