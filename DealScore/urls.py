from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DealScore.views.home', name='home'),
    # url(r'^DealScore/', include('DealScore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'dealapp.views.home', name='home'),
    url(r'^vote/(?P<deal_code>\d+)/$', 'dealapp.views.vote'),
    url(r'^show_deal/(?P<deal_code>\d+)/$', 'dealapp.views.show_deal'),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
