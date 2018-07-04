from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog_list, name='blog_list'),
    path('blog/<int:blog_pk>', views.blog_detail, name='blog_detail'),
    path('blog/<blog_tag>', views.comment_tag_list, name='comment_tag_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)