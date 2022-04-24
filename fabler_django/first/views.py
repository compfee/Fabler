from django.shortcuts import render


def index(request):
    return render(request, 'first/home.html')

def about(request):
    return render(request, 'first/about.html')

def projects(request):
    return render(request, 'first/projects.html')

def fabler(request):
    return render(request, 'first/fabler.html')