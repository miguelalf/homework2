from django.urls import path, include
from django.shortcuts import render, redirect

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar', views.create, name='create'),
    path('ver/<int:target>/', views.view, name='view'),
    path('actualizar/<int:target>/', views.update, name='update'),
    path('remover/<int:target>', views.delete, name='delete'),
]