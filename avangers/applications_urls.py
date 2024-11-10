from django.urls import path

from avangers.views import GetApplication, CreateApplication, UpdateApplication, GetByApplication, DeleteApplication

urlpatterns = [
    path('get/',GetApplication.as_view(),name='get'),
    path('get/<int:pk>/',GetByApplication.as_view(),name='get'),
    path('create/',CreateApplication.as_view(),name='create'),
    path('delete/<int:pk>/',DeleteApplication.as_view(),name='delete'),
    path('update/<int:pk>/',UpdateApplication.as_view(),name='update'),
]