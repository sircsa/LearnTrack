from django.shortcuts import render
from .models import Topic

def index(request):
    return render(request, 'learns_track/index.html')

def topics(request):
    #Page that show all topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learns_track/topics.html', context)
