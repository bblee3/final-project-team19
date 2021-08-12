from django.shortcuts import render

def index(request):
    return render(request, 'math4un/index.html')

def start(request):
    return render(request, 'math4un/start.html')

def settings(request):
    return render(request, 'math4un/settings.html')

def math(request):
    return render(request, 'math4un/math.html')

def correct(request):
    return render(request, 'math4un/correct.html')

def incorrect(request):
    return render(request, 'math4un/incorrect.html')