from rest_framework import serializers

from announcement.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Announcement
        fields = ['id', 'title', 'content', 'price', 'user', 'view_count']
