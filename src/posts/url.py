from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin
from posts import views

urlpatterns = [
    url(r'^create$', views.post_create),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    url(r'^$', views.post_list, name='list'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<id>\d+)/delete$', views.post_delete),

    # url(r'^posts/$', "<appname>.views.<function_name>"),
]
