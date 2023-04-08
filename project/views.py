from django.shortcuts import render, redirect


def index(request):
    return render(request, 'static_pages/index.html', {'h1': 'Главная страница'})
