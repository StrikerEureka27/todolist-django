from django.urls import include, path
from .views import TodoList, DetailTask, CreateTask, EditTask, DeleteTask, CustomLogin, CustomLogout

urlpatterns = [
    path('todo', TodoList.as_view(), name='todo'), 
    path('task/<int:pk>', DetailTask.as_view(), name='detail'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('edit-task/<int:pk>', EditTask.as_view(), name='edit-task'),
    path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete-task'),
    path("todo/login/", CustomLogin.as_view(), name='login'),
    path("todo/logout/", CustomLogout.as_view(), name='logout'),
]
