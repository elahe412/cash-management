from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from apps.user import views

app_name = "apps.user"
urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="create-user"),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("refresh/", jwt_views.TokenRefreshView.as_view(), name="token-refresh"),
    path("profile/", views.UserProfileView.as_view(), name="user-profile"),
]
