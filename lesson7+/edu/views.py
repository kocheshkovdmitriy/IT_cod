from django.shortcuts import render
from django.views.generic import ListView, DetailView
from edu.models import Test, Task, Section


class TestList(ListView):
    model = Test
    template_name = 'edu/list_tests.html'
    context_object_name = 'tests'

class TaskList(ListView):
    model = Task
    template_name = 'edu/list_tasks.html'
    context_object_name = 'tasks'

class TestDetail(DetailView):
    model = Test
    template_name = 'edu/detail_test.html'
    context_object_name = 'test'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['object'].title
        return context


class TaskDetail(DetailView):
    model = Task
    template_name = 'edu/detail_task.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['object'].__str__()
        return context