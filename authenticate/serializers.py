from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_info'] = {
            'id': self.user.id,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'email': self.user.email}
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class UserCreationSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "username", "password")
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'username': {'required': True},
        }

    def validate_password(self, value: str) -> str:
        return make_password(value)
