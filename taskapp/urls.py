from django.urls import path
from taskapp.views import *

urlpatterns=[
    path('', todolist, name='todolist'),
    path('delete/<task_id>',delete_task,name='delete_task'),
    path('edit/<task_id>',edit_task,name='edit_task'),
    path('complete/<task_id>',complete_task,name='complete_task'),
    path('pending/<task_id>',pending_task,name='pending_task'),
]