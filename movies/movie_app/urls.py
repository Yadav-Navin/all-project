from django.shortcuts import render
from django.urls import path
from movie_app import views

urlpatterns = [
    path('',views.Home,name='test'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('movies',views.movies,name='movies'),
    path('forgate',views.forgate,name='forgate'),
]