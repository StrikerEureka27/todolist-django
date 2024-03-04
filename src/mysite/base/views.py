from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Task

# Create your views here.

class CustomLogin(LoginView):
    
    def get_success_url(self) -> str:
        return reverse_lazy('todo')
    
class CustomLogout(LogoutView):
    def get_success_url(self) -> str:
        return reverse_lazy('login')


class TodoList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/todo_list.html'
    login_url = 'login'

class DetailTask(LoginRequiredMixin, PermissionRequiredMixin,  DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    permission_required = ['base.view_task']

class CreateTask(LoginRequiredMixin, PermissionRequiredMixin,  CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo')
    template_name = 'base/task_update.html'
    permission_required = ['base.view_task']

class EditTask(LoginRequiredMixin,PermissionRequiredMixin,  UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo')
    template_name = 'base/task_update.html'
    permission_required = ['base.view_task']

class DeleteTask(LoginRequiredMixin, PermissionRequiredMixin,  DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('todo')
    template_name = 'base/task_delete_confirmation.html'
    permission_required = ['base.view_task']