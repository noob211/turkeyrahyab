from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authenticate.views import CustomObtainTokenPairView, UserViewSet

app_name = "authenticate"

urlpatterns = [
    path('login/', CustomObtainTokenPairView.as_view(), name='login'),
    path('signup/', UserViewSet.as_view({"post": "create"}), name='signup'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
