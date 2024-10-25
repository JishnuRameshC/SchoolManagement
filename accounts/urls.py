from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path("logout/", views.UserLogoutView.as_view(), name="logout"), 
    path('register/', views.UserRegistrationView.as_view(), name='register'), 
    path('update/<int:user_id>/', views.UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:user_id>/', views.UserDeleteView.as_view(), name='user-delete'),
    path('change-password/<int:user_id>/', views.ChangePasswordView.as_view(), name='change-password'),  
]
