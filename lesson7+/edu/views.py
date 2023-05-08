from django.shortcuts import render
from django.views.generic import ListView
from edu.models import Test, Task, Section


class TestList(ListView):
    model = Test
    template_name = 'edu/list_tests.html'
    context_object_name = 'tests'

class TaskList(ListView):
    model = Task
    template_name = 'edu/list_tasks.html'
    context_object_name = 'tasks'
