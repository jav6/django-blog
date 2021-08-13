from django import urls
from django.urls import path

from . import views

urlpatterns = [
    # ex: /blog/
    path('', views.PostListView.as_view(), name='index'),
    # ex: /blog/post=5/
    path('post=<int:post_id>/', views.detail, name='detail'),
]