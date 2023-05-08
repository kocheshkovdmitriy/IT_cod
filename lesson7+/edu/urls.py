from django.urls import path
from edu.views import TaskList, TestList


app_name = 'edu'


urlpatterns = [
    path('list_tests/', TestList.as_view(), name='list_tests'),
    path('list_tasks/', TaskList.as_view(), name='list_tasks'),
]