from django.conf.urls import url

from .views import (
    create,
    launch,
    shut_down,
    bbu,
    delete,

    detail_utran,
    list,
    info,
)

urlpatterns = [
    url(r'^(?P<id>\d+)/create/$', create, name='create'),
    url(r'^(?P<id>\d+)/bbu/$', bbu, name='bbu'),
    url(r'^(?P<id>\d+)/launch/$', launch, name='launch'),
    url(r'^(?P<id>\d+)/shut_down/$', shut_down, name='shut_down'),
    url(r'^(?P<id>\d+)/delete/$', delete, name='delete'),

    url(r'^(?P<id>\d+)/$', detail_utran, name='detail_utran'),
    url(r'^(?P<id>\d+)/info/$', info, name='info'),
    url(r'^$', list, name="list"),
]
