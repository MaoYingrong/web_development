# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello World! I'm home.")
    return render(request, "home.html")

def about(request):
    # return HttpResponse("My about page.")
    return render(request, "about.html")

def html5tutorial(request):
    return render(request, "html5tutorial.html")

def css_example(request): 
    return render(request, "css_example.html")

def js_example(request):
    return render(request, "js_example.html")

