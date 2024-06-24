from django.urls import path

from .views import RegisterView, ProfileUpdateView, LoginView, LogoutConformationView


app_name = 'users_app'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('edit_profile/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutConformationView.as_view(), name='logout'),
]
