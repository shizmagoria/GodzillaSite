from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def godzilla_page(request):
    return render(request, 'godzilla.html')

def mothra_page(request):
    return render(request, 'mothra.html')

def rodan_page(request):
    return render(request, 'rodan.html')
