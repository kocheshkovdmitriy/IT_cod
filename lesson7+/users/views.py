from django.contrib.auth import login, authenticate, logout
from django.views import View
from users.models import Profile
from users.forms import RegisterForm, AuthUser

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
    def post(self, request):
        form = AuthUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    form.add_error('__all__', 'Учетная запись не активна.')
            else:
                form.add_error('__all__', 'Неверно введены имя пользователя или пароль.')
        context = {'form': form}
        return render(request, 'core/list_news.html', context=context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            slug = form.cleaned_data.get('username')
            city = form.cleaned_data.get('city')
            school = form.cleaned_data.get('school')
            grade = form.cleaned_data.get('grade')
            Profile.objects.create(user=user, slug=slug, city=city, school=school, grade=grade)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'core/list_news.html', context=context)
    else:
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'core/list_news.html', context=context)
