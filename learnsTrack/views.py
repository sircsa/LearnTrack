from django.shortcuts import render

def index(request):
    return render(request, 'learns_track/index.html')
