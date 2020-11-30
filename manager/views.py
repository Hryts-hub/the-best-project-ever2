from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("hello world")


def book_hello(request):
    return HttpResponse("hello book in the world")
# Create your views here.
