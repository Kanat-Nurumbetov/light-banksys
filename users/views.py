from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'masterpage/index.html')

def about(request):
    return render(request, 'masterpage/about.html')
