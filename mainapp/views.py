from django.shortcuts import render
from .fetch_data import *

def index(request):
    data = ""
    # data = main()
    return render(request, "index.html", {"ok":data})
