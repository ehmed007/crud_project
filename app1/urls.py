from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_student/', views.add_student),
    path('edit_student/<int:stu_id>/', views.edit_student, name='edit'),
    path('del_student/<int:stu_id>/', views.del_student, name='del'),
]
