from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def tictactoe(request):
    return render(request,'Tic Tac Toe/index.html')

def imagegallery(request):
    return render(request,'Image Gallery/index.html')

def clickcounter(request):
    return render(request,'Click Counter/index.html')

def videogalleryform(request):
    return render(request,'Video Gallery/index.html')

def videogallery(request):
    return render(request,'Video Gallery/VideoGallery.html')