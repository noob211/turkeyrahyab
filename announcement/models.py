from django.db import models
from uuid import uuid4
from django.conf import settings


class DateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Announcement(DateModel):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=150)
    content = models.TextField()
    price = models.PositiveIntegerField()
    is_verified = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_announcements')
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Announcement Info"
        verbose_name_plural = "Announcements"
        ordering = ["-created_at"]
