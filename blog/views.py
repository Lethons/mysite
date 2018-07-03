from django.shortcuts import render_to_response
from .models import Blog, Tag


def index(request):
    return render_to_response('index.html')


def blog_list(request):
    ctx = {}
    blogs = Blog.objects.all()
    ctx['blogs'] = blogs
    return render_to_response('blog_list.html', ctx)


def blog_detail(request):
    return render_to_response('blog_detail.html')