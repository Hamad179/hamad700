from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'clients/login.html')

def register_view(request):
    return render(request, 'clients/sinup.html')