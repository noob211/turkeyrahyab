from rest_framework.serializers import ModelSerializer
from userprofile.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
