from django.urls import path, include
from . import views


app_name = 'users'


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('register/', views.UserRegisterView.as_view(), name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.UserProfileView.as_view(), name="profile"),
]