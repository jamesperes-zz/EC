from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_dashboard),
    path('dashboard/', views.home_dashboard, name='home_dashboard'),
    path(
        'create-student/',
        views.create_student_view,
        name='create-student'
    ),
    path(
        'create-user/<user_type>',
        views.create_user_type_view,
        name='create-user'
    ),
    path('student/', views.user_detail, name='user_detail'),
    path('classrooms/', views.ClassRoomListView.as_view(), name='classroom_view'),
    path('classrooms/<slug:slug>/detail', views.ClassRoomDetailView.as_view(), name='classroom_detail_view'),
    path('classrooms/<slug:slug>/edit', views.ClassRoomUpdateView.as_view(), name='classroom_update_view'),
    path('classrooms/<slug:slug>/delete', views.ClassRoomDeactivateView.as_view(), name='classroom_delete_view'),
    path('classrooms/create/', views.ClassRoomCreateView.as_view(), name='classroom_create_view'),
    path('logout/', views.logout_view),
    path(
      'class/<int:class_room_id>/',
      views.list_classes_view,
      name='list_classes_view'
    ),
    path(
      'class/<int:class_id>/attendances/',
      views.class_view,
      name='class_view'
    ),
]
