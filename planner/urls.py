from django.urls import path
from .views import *

urlpatterns = [
    path('', MainTask.as_view(), name='planner_main'),
    path('create/', CreateTask.as_view(), name='task_create'),
    path('<int:pk>/', DetailTask.as_view(), name='task_detail'),
    path('delete/<int:pk>/', DeleteTask.as_view(), name='task_delete'),
    path('edit/<int:pk>/', EditTask.as_view(), name='task_edit'),
    path('time/add/<int:pk>/', AddTime.as_view(), name='time_add'),
    path('time/delete/<int:pk>/', DeleteTime.as_view(), name='time_delete'),
    path('tomato/add/<int:pk>/', add_tomato, name='add_tomato'),
]
