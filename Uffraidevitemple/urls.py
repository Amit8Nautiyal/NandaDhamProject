from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('uffraintemple/', views.uffraintemple, name='uffraintemple'),
]