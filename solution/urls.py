from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.solution_list.as_view(), name='solution_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.solution_details.as_view(), name='solution_details'),
    # url(r'^(?P<pk>[0-9]+)/edit$', views.solution_edit.as_view(), name='solution_edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.solution_delete, name='solution_delete'),

    ]