from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', 'treer.views.u_views',{'template_name':'index.html'}),
        url(r'^log/$', 'treer.views.u_views',{'template_name':'log.html'}),
        url(r'^contact/$', 'treer.views.contact'),
        url(r'^thanks/$', 'treer.views.thanks'),
        url(r'^blog/$', 'blog.views.blog_list', name='blog_list'),
        url(r'^code/$','blog.views.code_list',name='code_list'),
        url(r'^member/$','treer.views.u_views',{'template_name':'member.html'}),
        url(r'^admin$/', include(admin.site.urls)),
                       )
from django.conf import settings
if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
