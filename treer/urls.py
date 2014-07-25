from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$','treer.views.u_views',{'template_name':'index.html'}),
    url(r'^log/$','treer.views.u_views',{'template_name':'log.html'}),
    url(r'^member/$','treer.views.u_views',{'template_name':'member.html'}),
    url(r'^contact/$','treer.views.contact'),
    url(r'^thanks/$','treer.views.thanks'),
    # Examples:
    # url(r'^$', 'treer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
