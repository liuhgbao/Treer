from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
        url(r'^$', 'treer.views.u_views',{'template_name':'index.html'}),
        url(r'^log/$', 'blog.views.var_list',name='var_list'),
        url(r'^contact/$', 'treer.views.contact'),
        url(r'^thanks/$', 'treer.views.thanks'),
        url(r'^blog/$', 'blog.views.blog_list', name='blog_list'),
        url(r'^code/$','blog.views.code_list',name='code_list'),
        url(r'^member/$','blog.views.temp_list',name='temp_list'),
        url(r'^admin/', include(admin.site.urls)),
                       )

if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
    #TODO(Melodic): python manage.py collectstatic
