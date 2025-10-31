from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('bookshelf.urls')),  # si tu crées des urls pour l'app
]
