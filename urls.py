from django.conf import settings
from django.conf.urls.defaults import *
import blog
from blog.models import Post
from taggit.managers import TaggableManager
from taggit.views import tagged_object_list

exec "from %s import views" % settings.PROJECT_DIR

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
      (r'^admin/doc/', include('django.contrib.admindocs.urls')),
      (r'^admin/', include(admin.site.urls)),
      (r'^comments/', include('django.contrib.comments.urls')),
      (r'^articles/', include('blog.urls')),
      (r'^articles/tag/(?P<tag>[^/]+)/$', 'tagged_object_list', 
            dict(slug='tag', queryset='Post')),
      (r'^$', 'views.landing'),
)
