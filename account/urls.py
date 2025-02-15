from django.urls import path
from .views import LoginAPIView,RegisterAPIView,UserProfileAPIView
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path("register/", RegisterAPIView.as_view(), name="user-register"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),
]
