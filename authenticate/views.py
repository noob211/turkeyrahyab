from rest_framework import permissions, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

from authenticate.serializers import MyTokenObtainPairSerializer, UserCreationSerializer


class CustomObtainTokenPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer

