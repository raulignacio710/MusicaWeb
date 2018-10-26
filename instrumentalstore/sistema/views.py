from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',{})

def quienesomos(request):
    return render(request,'quienes.html',{})