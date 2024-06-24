from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users_app.urls')),
    path('', include('pages_app.urls')),
]
