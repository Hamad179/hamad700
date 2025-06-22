from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),       # عرض جميع المهام
    path('add/', views.add_task, name='add_task'),     # إضافة مهمة جديدة
]
