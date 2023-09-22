from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('enter_team', views.enter_team, name='enter_team'),
    path('view_tasks', views.tasks, name='tasks'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('done_task/<int:task_id>/', views.done_task, name='done_task'),
    path('create_team', views.create_team, name='create_team')
]