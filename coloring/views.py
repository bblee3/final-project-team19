from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def start(request):
    return render(request, 'coloring/start.html')

def settings(request):
    return render(request, 'coloring/settings.html')

def math(request):
    return render(request, 'coloring/math.html')

def correct(request):
    return render(request, 'coloring/correct.html')

def incorrect(request):
    return render(request, 'coloring/incorrect.html')