from django.urls import path
from users.views import profile


app_name = 'users'


urlpatterns = [
    path('profile/<int:user_pk>', profile, name='profile'),
]