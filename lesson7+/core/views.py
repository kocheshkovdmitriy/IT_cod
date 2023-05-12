from django.shortcuts import render
from django.views.generic import ListView, DetailView

from core.models import New, Commit


def about(request):
    return render(request=request, template_name='core/about.html')


class TitleMixin():
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context


class NewList(TitleMixin, ListView):
    model = New
    template_name = 'core/list_news.html'
    context_object_name = 'news'
    title = 'Новости'


class NewDetail(DetailView):
    model = New
    template_name = 'core/detail_new.html'
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['object'].title
        return context
