

# Create your views here.
from django.shortcuts import render

def landing_page(request):
    return render(request, 'index/landing.html')