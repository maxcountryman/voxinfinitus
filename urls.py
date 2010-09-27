from django.conf.urls.defaults import *
from django.conf import settings
exec "from %s import views" % settings.PROJECT_DIR

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
      (r'^admin/doc/', include('django.contrib.admindocs.urls')),
      (r'^admin/', include(admin.site.urls)),

      (r'^discover/', views.discover),
      (r'^services/', views.services),
      (r'^participate/', views.participate),

      (r'^$', 'views.landing'),
)
