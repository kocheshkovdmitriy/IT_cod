from users.models import Profile

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404


def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {
        'profile': profile,
        'title': profile.__str__()
    }
    return render(request, 'users/profile.html', context=context)
