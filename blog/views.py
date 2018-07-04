from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, Tag


def blog_paginator(req, blogs):
    """ blog paginator """
    ctx = {}
    page_num = req.GET.get('page', 1)
    pages = Paginator(blogs, 6)
    blogs = pages.page(page_num)
    current_page_num = blogs.number
    page_range = list(range(max(current_page_num-2, 1), min(current_page_num+2, pages.num_pages)+1))
    ctx['blogs'] = blogs
    ctx['pages'] = pages
    ctx['page_range'] = page_range
    return ctx



def index(request):
    ctx = {}
    blogs = Blog.objects.all()
    ctx['blogs'] = blogs
    return render_to_response('blog/index.html', ctx)


def blog_list(request):
    tags = Tag.objects.all()
    blogs = Blog.objects.all()
    ctx = blog_paginator(request, blogs)
    ctx['tags'] = tags
    return render_to_response('blog/blog_list.html', ctx)


def comment_tag_list(request, blog_tag):
    tags = Tag.objects.all()
    tag = get_object_or_404(Tag, tag=blog_tag)
    blogs = Blog.objects.filter(tag=tag)
    ctx = blog_paginator(request, blogs)
    ctx['tags'] = tags
    ctx['tag'] = tag
    return render_to_response('blog/comment_tag_list.html', ctx)


def blog_detail(request, blog_pk):
    ctx = {}
    blog = get_object_or_404(Blog, pk=blog_pk)
    ctx['blog'] = blog
    return render_to_response('blog/blog_detail.html', ctx)