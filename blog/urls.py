from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    (r'^(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<post_url>.+)$', 'show'),
    (r'^$', 'browse'),
)
#url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/(?P<object_id>\S+)/$', name='post_detail'),
