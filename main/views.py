from django.shortcuts import render
from django.http import HttpResponse
def index(request):

    data = {
        'title': 'Главная страница',
        'dict': {'name': 'Олег', 'surname': 'Иванов', 'second_name': 'Иванович'}
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})
# Create your views here.
