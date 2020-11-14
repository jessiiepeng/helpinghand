from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def tutoring(request):
    return render(request, 'pages/tutoring.html')

def about(request):
    return render(request, 'pages/about.html')

def sponsor(request):
    return render(request, 'pages/sponsor.html')
def login(request):
    return render(request, 'pages/login.html')

def contact(request):
    return render(request, 'pages/contact.html')

def apply(request):
    return render(request, 'pages/apply.html')