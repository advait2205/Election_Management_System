from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home),
    path('filter', views.filter),
    path('cast_vote', views.cast_vote),
    path('home', views.logged_user),
]
