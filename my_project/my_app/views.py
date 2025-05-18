from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    my_list = ['первый элемент', 'второй элемент', 'третий элемент', 'ctverty element']  # Список

    return render(request, 'index.html', {
        'my_list': my_list,
    })
    return render(request, "index.html", context)

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
