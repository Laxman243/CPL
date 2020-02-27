from django.shortcuts import render
from .models import Movie
from .engine import get_similar
from math import ceil
import csv,io
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'blog/index.html')


# Recommendation Engine call will go from here
def recommend(request):
    movielist = get_similar("Toy Story (1995)", 5)
    dicdata = movielist.to_dict()
    # print(dicdata)
    # print(type(movielist),"laxman")
    # n = len(dicdata)
    # print(movielist)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlides,'range': range(1,nSlides),'movie': dicdata}
    params = {'d':dicdata}
    return render(request, 'blog/recommend.html', params)


# For SignUp page request
def signup(request):
    return render(request, 'blog/signup.html')


# for Login Page request
def login(request):
    return render(request, 'blog/login.html')


# for Logout page request
def logout(request):
    return render(request, 'blog/logout.html')




