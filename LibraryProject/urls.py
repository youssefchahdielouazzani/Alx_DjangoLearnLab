from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 🔽 On inclut ici les URLs de l'application relationship_app
    path('', include('relationship_app.urls')),
]



