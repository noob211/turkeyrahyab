from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from announcement.permissions import IsOwner, IsOwnerOrAdmin
from announcement.serializers import AnnouncementSerializer
from announcement.models import Announcement
from announcement.filters import AnnouncementFilter


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnnouncementFilter

    @action(detail=True, methods=['GET'], permission_classes=[IsOwnerOrAdmin])
    def view(self, request, pk=None):
        obj = self.get_object()
        return Response({"total_views": obj.view_count}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.view_count = obj.view_count + 1
        obj.save(update_fields=("view_count",))
        return super().retrieve(request, *args, **kwargs)

    def get_permissions(self):
        if self.request.method in {'PUT', 'DELETE'}:
            return [IsOwnerOrAdmin()]
        return super(AnnouncementViewSet, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response({"message": serializer.data}, status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'], permission_classes=[IsAdminUser])
    def accept(self, request, pk=None):
        announcement = self.get_object()
        announcement.is_verified = True
        announcement.save()
        return Response({"message": f'announcement {announcement.title} has accepted'}, status=status.HTTP_200_OK)


class MyAnnouncementViewSet(ReadOnlyModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AnnouncementFilter

    def get_queryset(self):
        queryset = self.filter_queryset(self.get_queryset())
        return queryset.filter(user=self.request.user)
