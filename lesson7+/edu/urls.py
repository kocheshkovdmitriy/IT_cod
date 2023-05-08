from django.urls import path
from edu.views import TaskList, TestList, TaskDetail, TestDetail


app_name = 'edu'


urlpatterns = [
    path('list_tests/', TestList.as_view(), name='list_tests'),
    path('list_tasks/', TaskList.as_view(), name='list_tasks'),
    path('test/<int:pk>', TestDetail.as_view(), name='detail_test'),
    path('task/<int:pk>', TaskDetail.as_view(), name='detail_task'),
]