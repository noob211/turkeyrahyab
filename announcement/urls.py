from django.urls import path, include
from rest_framework.routers import DefaultRouter
from announcement.views import AnnouncementViewSet, MyAnnouncementViewSet

app_name = 'announcement'

router = DefaultRouter()

router.register('announcements', AnnouncementViewSet)
router.register('my-announcements', MyAnnouncementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
