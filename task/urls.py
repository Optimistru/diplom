from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.task_list.as_view(), name='task_list'),
    url(r'^/(?P<pk>[0-9]+)/$', views.task_details.as_view(), name='task_details'),
    url(r'^/(?P<pk>[0-9]+)/edit$', views.task_edit.as_view(), name='task_edit'),
    url(r'^/(?P<pk>[0-9]+)/delete$', views.task_delete.as_view(), name='task_delete'),

    url(r'^/mod(?P<pk>[0-9]+)/edit$', views.mod_task_edit.as_view(), name='mod_task_edit'),
    url(r'^/mod(?P<pk>[0-9]+)/delete$', views.mod_task_delete.as_view(), name='mod_task_delete'),

]