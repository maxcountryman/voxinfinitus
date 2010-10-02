import re
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list

POSTS_PER_PAGE = 6

def show(request, year, month, post_url):
    year = int(year)
    month = int(month)
    try:
        start = datetime(year, month, 1)
        if month == 12:
            end = datetime(year+1, 1, 1)
        else:
            end = datetime(year, month+1, 1)
    except ValueError:
        raise Http404('Date format incorrect')
    post = get_object_or_404(Post, slug=post_url, date_published__gte=start, 
        date_published__lt=end)
    return show_post(request, post)

def show_post(request, post):
    recent_posts = Post.objects.filter()
    recent_posts = recent_posts.order_by('-date_published')[:6]

    return direct_to_template(request, 'blog/post_detail.html',
        {'post': post, 'recent_posts': recent_posts,})

def browse(request):
    query = Post.objects.filter()
    query = query.order_by('-date_published')
    return object_list(request, query, paginate_by=POSTS_PER_PAGE,
        extra_context={'recent_posts': query[:6],
                       'browse_posts': True})

def browse_tagged_posts(request, tag):
    query = Post.objects.filter(tags=tag)
    query = query.order_by('-date_published')
    return object_list(request, query, paginate_by=POSTS_PER_PAGE,
        extra_context={'recent_posts': query[:6],
                       'browse_posts': True})
