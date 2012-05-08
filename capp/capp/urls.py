from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'capp.views.home', name='home'),
    # url(r'^capp/', include('capp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT}),
#    url(r'', '')
    url(r'^register/$', 'register.views.register', name='register'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'login.views.doLogin', name='login'),
    url(r'^logout/$', 'login.views.doLogout', name='logout'),
    url(r'', include('django.contrib.flatpages.urls')),
)
