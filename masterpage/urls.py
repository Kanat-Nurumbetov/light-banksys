from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('auth', views.auth),
    path('registration', views.registration),
]