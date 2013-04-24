from django.conf.urls import patterns, include, url
from base.views import about, index, current_time
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #base nav
    url(r'^$', index),
    url(r'^blog/', include('blog.urls')),
    url(r'^about/$', about),
    url(r'^lab$', current_time),
    url('^lab/time/$', current_time),

    #login and logout
    url(r'^accounts/login/(?P<next>\.+)/$', 'base.views.login'),

    #static files
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),

    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # end admin
)
