from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return HttpResponse('<h1>About the CatCollector</h1>')