from django.urls import path
from userprofile.views import ProfileApiView

app_name = 'userprofile'

urlpatterns = [
    path('profile/', ProfileApiView.as_view(), name='profile_detail')
]
