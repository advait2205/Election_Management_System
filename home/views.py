from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request, "login.html")

def filter(request):
    return render(request, "filter_page.html")

def cast_vote(request):
    return render(request, "voting.html")

def logged_user(request):
    return render(request, "logged_user.html")

