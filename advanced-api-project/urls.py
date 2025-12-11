from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),     # Admin Django
    path('api/', include('api.urls')),   # Inclusion des URLs de l'application API
]
