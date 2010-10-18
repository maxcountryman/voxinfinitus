from django.conf import settings
from django.conf.urls.defaults import *
from blog.models import Post, PostsSitemap
from django.contrib.sitemaps import FlatPageSitemap 
import views
import taggit

sitemaps = { 
     'flatpages': FlatPageSitemap,
     'blog': PostsSitemap,
     } 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
      (r'^admin/doc/', include('django.contrib.admindocs.urls')),
      (r'^admin/', include(admin.site.urls)),
      (r'^grappelli/', include('grappelli.urls')),
      (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
      (r'^blog/', include('blog.urls')),
      (r'^tag/(?P<slug>[^/]+)/$', 'taggit.views.tagged_object_list', 
            dict(queryset=Post.objects.all(),template_name='taggit/post_list.html')),
      (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
      (r'^$', 'views.landing'),
)
