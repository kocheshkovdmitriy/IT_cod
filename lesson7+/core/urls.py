from django.urls import path
from core.views import NewList, NewDetail, about

app_name = 'core'


urlpatterns = [
    path('', NewList.as_view(), name='list_news'),
    path('new/<int:pk>', NewDetail.as_view(), name='detail_new'),
    path('about/', about, name='about'),
]