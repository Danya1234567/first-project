from django.urls import path

from avangers.views import GetCreateComments, UpdateComments, DeleteComment

urlpatterns = [
    path('<int:pk>',GetCreateComments.as_view(),name='Get'),
    path('update/<int:pk>',UpdateComments.as_view(),name='Update'),
    path('delete/<int:pk>',DeleteComment.as_view(),name='delete'),

]