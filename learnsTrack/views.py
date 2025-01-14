from django.shortcuts import render
from .models import Topic

#Home page
def index(request):
    return render(request, 'learns_track/index.html')

#Page that show all topics
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learns_track/topics.html', context)

#A single topic and all its entries
def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learns_track/topic.html', context)
