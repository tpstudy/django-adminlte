from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # 保持原来的逻辑，渲染 'pages/index.html' 模板
    return render(request, 'pages/index.html')
