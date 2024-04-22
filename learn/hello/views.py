from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hello/index.html")
def Joe(requests):
    return HttpResponse("Hello, Joe!")

def greet(request, names):
    return HttpResponse(f"Hello {names.capitalize()}")
