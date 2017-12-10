from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.ec_home),
    url(r'^dashboard/', views.home_dashboard, name='home_dashboard'),
    url(r'^student/', views.user_detail, name='user_detail'),
    url(r'^register/$', views.register),
    url(r'^calendar/$', views.calendar_view, name='calendar_view'),
    url(r'^logout/$', views.logout_view),
]
