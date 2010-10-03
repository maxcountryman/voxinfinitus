from django.conf.urls.defaults import *
from blog.views import RssNewsFeed, AtomNewsFeed

urlpatterns = patterns('blog.views',
    (r'^(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<post_url>.+)$', 'show'),
    (r'^rss/$', RssNewsFeed()),
    (r'^atom/$', AtomNewsFeed()),
    (r'^$', 'browse'),
)
