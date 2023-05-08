from profile import Profile

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404


def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    profile = get_object_or_404(Profile, user=user)
    context = {
        'profile': profile
    }
    return render(request, 'users/profile.html', context=context)
