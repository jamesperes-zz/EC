from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_dashboard),
    path('dashboard/', views.home_dashboard, name='home_dashboard'),
    path('student/', views.user_detail, name='user_detail'),
    path('classroom/', views.classroom_view, name='classroom_view'),
    path('logout/', views.logout_view),
    path('class/', views.classes_view, name='classes_views'),
    path('class/<int:class_id>/attendances/', views.class_view, name='class_view'),
]
