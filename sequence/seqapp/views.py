from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello in the Django world!!")