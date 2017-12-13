from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.home_dashboard),
    url(r'^dashboard/', views.home_dashboard, name='home_dashboard'),
    url(r'^student/', views.user_detail, name='user_detail'),
    url(r'^calendar/$', views.calendar_view, name='calendar_view'),
    url(r'^classroom/$', views.classroom_view, name='classroom_view'),
    url(r'^logout/$', views.logout_view),
]
