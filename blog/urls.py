from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    (r'^(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<post_url>.+)$', 'show'),
    (r'^$', 'browse'),
)
