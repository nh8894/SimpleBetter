from django.conf.urls import url, include
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
]