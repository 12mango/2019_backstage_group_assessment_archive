from django.conf.urls import include, url
from django.contrib import admin
from newsApp import views as newsAppViews

urlpatterns = [

    url(r'^$', newsAppViews.index, name='index'),
    url(r'^tableAll/$',newsAppViews.tableAll,name='tableAll'),
    url(r'^table/$', newsAppViews.table, name='table'),
    url(r'^admin/$', include(admin.site.urls)),
]
