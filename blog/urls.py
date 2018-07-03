from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs', views.blog_list, name='blog_list'),
    path('blogs/1', views.blog_detail, name='blog_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)