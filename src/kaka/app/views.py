from django.shortcuts import render
from django.http import HttpResponse

# All Views

def index(request):
    return render(request, "index.html")