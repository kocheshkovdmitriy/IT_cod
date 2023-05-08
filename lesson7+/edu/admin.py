from django.contrib import admin
from edu.models import Task, Test, Section

@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ['task', 'section']


@admin.register(Test)
class Test(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Section)
class Section(admin.ModelAdmin):
    list_display = ['title']