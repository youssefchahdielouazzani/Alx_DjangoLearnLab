"""api_project URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # On inclura plus tard les URLs de l'app api
    # path('api/', include('api.urls')),
]

