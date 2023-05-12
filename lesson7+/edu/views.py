from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from edu.models import Test, Task, Section

class TitleMixin():
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context


class TestList(TitleMixin, ListView):
    model = Test
    template_name = 'edu/list_tests.html'
    context_object_name = 'tests'
    title = 'Каталог тестов'


class TaskList(TitleMixin, ListView):
    model = Task
    template_name = 'edu/list_tasks.html'
    context_object_name = 'tasks'
    title = 'Каталог заданий'


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


class TaskCreate(TitleMixin, CreateView):
    model = Task
    template_name = 'edu/task_create.html'
    fields = '__all__'
    title = 'Создание задачи'
    success_url = reverse_lazy("edu:list_tasks")


class TaskUpdate(TitleMixin, UpdateView):
    model = Task
    template_name = 'edu/task_update.html'
    fields = '__all__'
    title = 'Изменение задачи'

    def get_success_url(self):
        return reverse_lazy("edu:detail_task", kwargs={'pk': self.object.pk})


class TaskDelete(TitleMixin, DeleteView):
    model = Task
    template_name = 'edu/task_delete.html'
    title = 'Удаление задачи'
    success_url = reverse_lazy("edu:list_tasks")