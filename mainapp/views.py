from django.shortcuts import render
# mainapp/views.py
from django.http import JsonResponse
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # Ensure BASE_DIR is defined

def debug_static_files(request):
    static_root = os.path.join(BASE_DIR, 'staticfiles_build', 'staticfiles')
    files = []
    for root, dirs, filenames in os.walk(static_root):
        for filename in filenames:
            files.append(os.path.relpath(os.path.join(root, filename), static_root))
    return JsonResponse(files, safe=False)


def index(request):
    data = ""
    # data = main()
    return render(request, "index.html", {"ok":data})
