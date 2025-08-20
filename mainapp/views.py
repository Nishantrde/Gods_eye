from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index2.html")
def index_test(request):
    return render(request, "data_visualizer.html")

