from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_list.as_view(), name='user_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.user_details.as_view(), name='user_details'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.user_edit.as_view(), name='user_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.user_delete, name='user_delete'),
]