from django.conf import settings
from django.conf.urls.defaults import *
import views
from blog.models import Post, PostsSitemap 
import taggit
from django.contrib.sitemaps import FlatPageSitemap 

sitemaps = { 
     'flatpages': FlatPageSitemap,
     'blog': PostsSitemap,
     } 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
      (r'^admin/doc/', include('django.contrib.admindocs.urls')),
      (r'^admin/', include(admin.site.urls)),
      (r'^comments/', include('django.contrib.comments.urls')),
      (r'^articles/', include('blog.urls')),
      (r'^articles/tag/(?P<slug>[^/]+)/$', 'taggit.views.tagged_object_list', 
            dict(queryset=Post.objects.all(),template_name='taggit/post_list.html')),
      (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
      (r'^$', 'views.landing'),
)
