from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:blog_pk>', views.blog_detail, name='blog_detail'),
    path('blog/<blog_tag>', views.comment_tag_list, name='comment_tag_list'),
    path('aboutme', views.about_me, name='about_me'),
]

handler404 = views.page_not_found