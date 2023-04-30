from django.shortcuts import render
from django.template import Template, Context

def list_person(request):
    context = {'persons': [
            {'name': 'Victor', 'post': 'menedger'},
            {'name': 'Liza', 'post': 'menedger'},
            {'name': 'Dmitrii', 'post': 'menedger'},
            {'name': 'Sveta', 'post': 'menedger'}
        ]}
    return render(request, 'core/list_person.html', context=context)

def info_person(request):
    context = {'name': 'Victor',
             'post': 'menedger',
             'phone': 123456789,
             'email': 'viv@ya.ru',
             'adress': 'st. pushkina d. 138'}
    return render(request, 'core/info_person.html', context=context)


