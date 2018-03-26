from django.conf.urls import url
from . import views

app_name = 'boards'

urlpatterns = [
    url(r'^$', views.MyListView.as_view(), name='index'),
    url(r'^boards$', views.MyListView.as_view(), name='list'),
    url(r'^boards/(?P<pk>\d+)$', views.BoardDetail.as_view(),
        name='board_detail'),
    url(r'^boards/(?P<pk>\d+)/new$', views.new_topic, name='board_new'),

]
