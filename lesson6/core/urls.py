from django.urls import path
from core.views import info_person, list_person

urlpatterns = [
    path('', list_person, name='list_person'),
    path('info/', info_person, name='info_person'),
]