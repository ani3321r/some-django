from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to homepage")
    return render(request, 'homepage/index.html')

def about(request):
    # return HttpResponse("Welcome to about page")
    return render(request, 'aboutPage/index.html')

def contactUs(request):
    # return HttpResponse("Welcome to contact us page")
    return render(request, 'contactPage/index.html')