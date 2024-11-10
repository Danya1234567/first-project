from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from app.views import TechniqueDeleteView, TechniqueCreateView, TechniqueListView, TechByidView

urlpatterns = [
    path('all/', TechniqueListView.as_view(), name='technique-list'),
    path('<int:pk>/', TechByidView.as_view(), name='technique-detail'),
    path('create/', TechniqueCreateView.as_view(), name='technique-create'),
    path('delete/<int:pk>/', TechniqueDeleteView.as_view(), name='technique-delete'),
]