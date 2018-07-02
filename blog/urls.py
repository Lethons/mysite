from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs', views.blog_list, name='blog_list'),
]