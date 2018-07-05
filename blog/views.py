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


def left_comment_date():
    """ get left part comment date """
    ctx = {}
    tags = Tag.objects.all()
    commend_blogs = Blog.objects.filter(is_commend=True)
    ctx['tags'] = tags
    ctx['commend_blogs'] = commend_blogs
    return ctx


def home(request):
    blogs = Blog.objects.all()
    ctx = left_comment_date()
    ctx['blogs'] = blogs
    return render_to_response('blog/index.html', ctx)


def blog_list(request):
    blogs = Blog.objects.all()
    ctx1 = blog_paginator(request, blogs)
    ctx2 = left_comment_date()
    ctx = dict(ctx1, **ctx2)
    return render_to_response('blog/blog_list.html', ctx)


def comment_tag_list(request, blog_tag):
    tag = get_object_or_404(Tag, tag=blog_tag)
    blogs = Blog.objects.filter(tag=tag)
    ctx1 = blog_paginator(request, blogs)
    ctx2 = left_comment_date()
    ctx = dict(ctx1, **ctx2)
    ctx['tag'] = tag
    return render_to_response('blog/comment_tag_list.html', ctx)


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    blogs = Blog.objects.all()
    ctx = left_comment_date()
    ctx['blogs'] = blogs
    ctx['blog'] = blog
    return render_to_response('blog/blog_detail.html', ctx)


def about_me(request):
    return render_to_response('blog/about_me.html')


def page_not_found(request):
    return render_to_response('404.html')
