from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from userprofile.models import Profile
from userprofile.serializers import ProfileSerializer
from django.shortcuts import get_object_or_404


class ProfileApiView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(self.queryset, user=self.request.user)
