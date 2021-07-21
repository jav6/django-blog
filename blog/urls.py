from django import urls
from django.urls import path

from . import views

urlpatterns = [
    # ex: /blog/
    path('', views.index, name='index'),
    # ex: /blog/post=5/
    path('post=<int:post_id>/', views.detail, name='detail'),
]