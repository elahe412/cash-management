from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from apps.user.models import CustomUser, Profile
from apps.user.serializers import RegisterSerializer, ProfileSerializer


class UserRegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    http_method_names = ['post']


class UserProfileView(ListAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
