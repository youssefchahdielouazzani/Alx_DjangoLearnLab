from django.contrib import admin
from django.urls import path
from relationship_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.library_list, name='library_list'),  # Exemple de vue
]

