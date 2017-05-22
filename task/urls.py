from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.task_list.as_view(), name='task_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.task_details.as_view(), name='task_details'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.task_edit.as_view(), name='task_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.task_delete, name='task_delete'),

    # url(r'^(?P<pk>[0-9]+)/$', views.task_mod_details.as_view(), name='task_mod_details'),
    # url(r'^(?P<pk>[0-9]+)/edit$', views.task_mod_edit.as_view(), name='task_mod_edit'),
    # url(r'^(?P<pk>[0-9]+)/delete$', views.task_mod_delete, name='task_mod_delete'),
]