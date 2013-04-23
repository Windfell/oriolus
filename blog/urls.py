__author__ = 'liwenchao'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
                       url(r'^$', 'blog_list'),
                       url(r'^page/(?P<id>\d+)$', 'blog_list'),
                       url(r'^(?P<id>\d+)/$', 'blog_show', name='detailblog'),
                       url(r'^add/$', 'blog_add', name='addblog'),
                       url(r'^delete/(?P<id>\d+)$', 'delete_blog', name='deleteblog')
)