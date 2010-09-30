import re
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post
from django.views.generic.simple import direct_to_template

def show(request, year, month, post_url):
    try:
        start = datetime(int(year), int(month), 1)
        if month == 12:
            end = datetime(int(year)+1, 1, 1)
        else:
            end = datetime(int(year), int(month)+1, 1)
    except ValueError:
        raise Http404('Date format incorrect')
    post = get_object_or_404(Post, slug=post_url, date_published__gte=start, 
        date_published__lt=end)
    return show_post(request, post)

def show_post(request, post):
    recent_posts = Post.objects.filter()
    recent_posts = recent_posts.order_by('-published_on')[:6]

    return direct_to_template(request, 'post_detail.html',
        {'post': post, 'recent_posts': recent_posts,})
