from django.conf.urls import include, url
from django.contrib import admin
from os import path

from task import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'pmanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.sign_in, name='home'), #TEMP

    url(r'^admin/', include(admin.site.urls)),
    url(r'contest', include('contest.urls')),
    url(r'task', include('task.urls')),
    url(r'^lk$', views.lk, name='lk'),
]
