from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'geologic_time.views.home', name='home'),
    url(r'^help/', 'geologic_time.views.help', name='help'),
    url(r'^config/', 'geologic_time.views.config', name='config'),
    url(r'^alerts/', 'geologic_time.views.alerts', name='alerts'),
    # url(r'^geologic_time/', include('geologic_time.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
