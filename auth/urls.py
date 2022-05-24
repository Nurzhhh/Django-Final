from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

app_name = 'auth'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='auth_login'),
    # path('register/', RegisterView.as_view(), name='auth_register'),
    # path('logout/', LogoutView.as_view(), name='auth_logout'),
]