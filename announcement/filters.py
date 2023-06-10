from django_filters import rest_framework as filters, CharFilter
from announcement.models import Announcement


class AnnouncementFilter(filters.FilterSet):

    class Meta:
        model = Announcement
        fields = {
            'view_count': ['exact', 'lt', 'gt'],
            'created_at': ['exact', 'gt'],
            'is_verified': ['exact'],
        }

