from django.contrib import admin
from users.models import Profile

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ['user', 'city', 'school', 'grade']
