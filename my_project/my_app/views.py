from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def hello(request):
    names = ['Иван', 'Мария', 'Алексей']
    is_logged_in = True
    user_age = 25

    return render(request, 'index.html', {
        'names': names,
        'is_logged_in': is_logged_in,
        'user_age': user_age,
    })

def hello(request, name):
    print(name)
    return HttpResponse(f"Heloo Helouuu, {name}))")

def number(request, num):
    print(num)
    return HttpResponse(f"Heloo Helouuu, {num * 3}))")

def hello_id(request, user_id):
    return HttpResponse(f"Привет, пользователь с ID {user_id}!")

def hello_slug(request, slug): # <-- добавляем новый маршрут
    return HttpResponse(f"Привет, {slug}!")
