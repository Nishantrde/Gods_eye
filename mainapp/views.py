from django.shortcuts import render
from .models import library
from datetime import date
import json

# Create your views here.
def index(request):
    yt_data = ""
    yt_data = library.objects.filter(id=str(date.today()))
    if yt_data:
        yt_data = library.objects.get(id=str(date.today()))
    else:
        with open('C:/Users/ACER/Downloads/yt_world/yt_world/top_trending_videos.json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        
        check_exist = library.objects.filter(id=str(date.today()))
        if not check_exist:
            yt_data = library(id = str(date.today()), data = json_data)
            yt_data.save()
    print("here",yt_data.data["India"])

    return render(request, "index2.html", {"data":yt_data.data})
def index_test(request):
    return render(request, "data_visualizer.html")
def re_gen(request):
    with open('C:/Users/ACER/Desktop/gods_eye/gods_eye/top_trending_videos.json', 'r', encoding='utf-8') as file:
        yt_data = json.load(file)
    
    check_exist = library.objects.filter(id=str(date.today()))
    if not check_exist:
        con_dit = library(id = str(date.today()), data = yt_data)
        con_dit.save()
    else: print("Alredy exist!")
    return render(request, "data_visualizer.html")

