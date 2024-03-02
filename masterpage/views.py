from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'masterpage/index.html')

def auth(request):
    return render(request, 'masterpage/auth.html')

def registration(request):
    return render(request, 'masterpage/registration.html')