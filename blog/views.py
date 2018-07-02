from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html')


def blog_list(request):
    return render_to_response('blog_list.html')