from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name='chatroom'

urlpatterns=[
    path(r'^$',views.index,name='index '),
    #url(r'^$', views.index, name="Chat Room")
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room')
]