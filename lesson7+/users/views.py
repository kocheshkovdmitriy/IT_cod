from django.contrib.auth import login, authenticate, logout
from django.views import View
from users.models import Profile

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect


def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {
        'profile': profile,
        'title': profile.__str__()
    }
    return render(request, 'users/profile.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('/')

class LoginView(View):
    def get(self, request):
        return redirect('/')

    def post(self, request):
        return redirect('/')

def register_view(request):
    return redirect('/')
