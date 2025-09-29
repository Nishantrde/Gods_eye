from django.shortcuts import render
from .models import library
from datetime import date
import json
from .yt_api_local import fetch

# Create your views here.
def index(request):
    yt_data = ""
    yt_data = library.objects.filter(id=str(date.today()))
    if yt_data: 
        yt_data = library.objects.get(id=str(date.today()))
    else:
        json_data = fetch() 
        
        check_exist = library.objects.filter(id=str(date.today()))
        if not check_exist:
            yt_data = library(id = str(date.today()), data = json_data)
            yt_data.save()
    print("here",yt_data.data["India"])

    return render(request, "index2.html", {"data":yt_data.data})
def index_test(request):
    return render(request, "data_visualizer.html")
def re_gen(request):
    yt_data = fetch()
    
    check_exist = library.objects.filter(id=str(date.today()))
    if not check_exist:
        con_dit = library(id = str(date.today()), data = yt_data)
        con_dit.save()
    else: print("Alredy exist!")
    return render(request, "data_visualizer.html")

