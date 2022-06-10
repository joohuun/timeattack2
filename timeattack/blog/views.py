from django.shortcuts import render
from .models import Category, Article


# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request, 'new.html')
    # elif request.method == 'POST':
