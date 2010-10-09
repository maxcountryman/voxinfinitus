import re
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, Post
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.contrib.comments import Comment

POSTS_PER_PAGE = 6

def show(request, blog_url, year, month, post_url):
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
    blog = get_object_or_404(Blog, base_url=blog_url)
    post = get_object_or_404(Post, slug=post_url, date_published__gte=start, 
        date_published__lt=end)
    return show_post(request, blog, post)

def show_post(request, blog, post):
    recent_posts = Post.objects.filter(blog=blog)
    recent_posts = recent_posts.order_by('-date_published')[:6]

    return direct_to_template(request, 'blog/post_detail.html',
        {'post': post, 'blog': blog, 'recent_posts': recent_posts,})

def browse(request, blog_url):
    blog = get_object_or_404(Blog, base_url=blog_url)
    query = Post.objects.filter(blog=blog)
    query = query.order_by('-date_published')
    return object_list(request, query, paginate_by=POSTS_PER_PAGE,
        extra_context={'blog': blog, 'recent_posts': query[:6],
                       'browse_posts': True})

def comment_posted(request):
    if request.GET['c']:
        comment_id = request.GET['c']
        comment = Comment.objects.get(pk=comment_id)
        post = Post.objects.get(id=comment.object_pk)
        if post:
            return HttpResponseRedirect(post.get_absolute_url())
    return HttpResponseRedirect("/")

class RssNewsFeed(Feed):
    title = "Vox Infinitus"
    link = "/articles/"
    description = "A feed of recent articles on VoxInfinitus.net."

    def items(self):
        return Post.objects.order_by('-date_published')[:5]

class AtomNewsFeed(RssNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssNewsFeed.description

