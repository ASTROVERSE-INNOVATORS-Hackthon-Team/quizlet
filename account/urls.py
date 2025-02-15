from django.urls import path
from .views import LoginAPIView,RegisterAPIView,UserProfileAPIView,LogoutAPIView,UpdateProfileView
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path("register/", RegisterAPIView.as_view(), name="user-register"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("api/v1/update-profile/", UpdateProfileView.as_view(), name="update-profile"),


]
