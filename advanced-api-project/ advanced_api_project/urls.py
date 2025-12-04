from django.contrib import admin
from django.urls import path
from advanced_api_project.views import BookListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', BookListView.as_view()),
]

