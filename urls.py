from django.conf import settings
from django.conf.urls.defaults import *
import blog
import taggit
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
      (r'^admin/doc/', include('django.contrib.admindocs.urls')),
      (r'^admin/', include(admin.site.urls)),
      (r'^comments/', include('django.contrib.comments.urls')),
      (r'^articles/', include('blog.urls')),
      (r'^articles/tag/(?P<slug>[^/]+)/$', 'taggit.views.tagged_object_list', 
            dict(queryset=blog.models.Post.objects.all(),template_name='taggit/post_list.html')),
      (r'^$', 'views.landing'),
)
