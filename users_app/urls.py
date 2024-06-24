from django.urls import path

from .views import LoginView, LogoutConformationView


app_name = 'users_app'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutConformationView.as_view(), name='logout'),
]
