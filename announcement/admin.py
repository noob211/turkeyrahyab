from django.contrib import admin
from announcement.models import Announcement


@admin.register(Announcement)
class AdminAnnouncement(admin.ModelAdmin):
    list_display = ["title", "user", "price", "created_at", "view_count"]
    search_fields = ["title", "content"]
    list_filter = ["user"]
    date_hierarchy = "created_at"
