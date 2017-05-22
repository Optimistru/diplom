from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contest_list.as_view(), name='contest_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.contest_details.as_view(), name='contest_details'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.contest_edit.as_view(), name='contest_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.contest_delete, name='contest_delete'),
]