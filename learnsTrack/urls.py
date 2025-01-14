from django.urls import path
from . import views

app_name = 'learns_track'
urlpatterns = [
    #Home page
    path('', views.index, name ='index'),
    #Show all topics page
    path('topics/', views.topics, name = 'topics'),
    #Page for a single topic
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
]
