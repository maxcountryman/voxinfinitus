from django.conf.urls.defaults import *
from blog.views import RssNewsFeed, AtomNewsFeed

urlpatterns = patterns('blog.views',
    (r'^(?P<blog_url>[^/]+)/(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<post_url>.+)$', 'show'),
    (r'^(?P<blog_url>[^/]+)/$', 'browse'),
    (r'^(?P<blog_url>[^/]+)/rss/$', RssNewsFeed()),
    (r'^(?P<blog_url>[^/]+)/atom/$', AtomNewsFeed()),
)
