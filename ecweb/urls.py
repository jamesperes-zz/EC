from django.conf.urls import include, url
from django.urls import path

from . import views


urlpatterns = [
    url(r'^$', views.home_dashboard),
    url(r'^dashboard/', views.home_dashboard, name='home_dashboard'),
    url(r'^student/', views.user_detail, name='user_detail'),
    url(r'^classrooms/$', views.ClassRoomListView.as_view(), name='classroom_view'),
    path('classrooms/<slug:slug>/detail', views.ClassRoomDetailView.as_view(), name='classroom_detail_view'),
    path('classrooms/<slug:slug>/edit', views.ClassRoomUpdateView.as_view(), name='classroom_update_view'),
    path('classrooms/<slug:slug>/delete', views.ClassRoomDeactivateView.as_view(), name='classroom_delete_view'),
    url(r'^classrooms/create/$', views.ClassRoomCreateView.as_view(), name='classroom_create_view'),
    url(r'^logout/$', views.logout_view),
    url(r'^class/$', views.classes_view, name='classes_views'),
    url(r'^class/(?P<class_id>[0-9]+)/attendances/$', views.class_view, name='class_view'),
]
