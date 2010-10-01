from django.conf import settings
from django.conf.urls.defaults import *
exec "from %s import views" % settings.PROJECT_DIR
import blog

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
      (r'^admin/doc/', include('django.contrib.admindocs.urls')),
      (r'^admin/', include(admin.site.urls)),

      (r'articles/', include('blog.urls')),

      (r'^$', 'views.landing'),
)

