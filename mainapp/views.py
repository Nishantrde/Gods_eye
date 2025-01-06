from django.shortcuts import render


def index(request):
    data = ""
    # data = main()
    return render(request, "index.html", {"ok":data})
