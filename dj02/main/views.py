from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'caption': "CatDjango",
        'caption2': "qqq"
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def animals(request):
    return render(request, 'main/animals.html')

def personal(request):
    return render(request, 'main/personal.html')
