from django.conf import settings
from django.conf.urls.defaults import *
import blog
import taggit
exec "from %s import views" % settings.PROJECT_DIR

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
      (r'^admin/doc/', include('django.contrib.admindocs.urls')),
      (r'^admin/', include(admin.site.urls)),
      (r'^comments/', include('django.contrib.comments.urls')),
      (r'^articles/', include('blog.urls')),
      (r'^articles/tag/(?P<tag>[^/]+)/$', 'taggit.views.tagged_object_list', 
            dict(slug='tag', queryset=blog.Post.objects.all())),
      (r'^$', 'views.landing'),
)
