from django.urls import path
from . import views

app_name = 'learns_track'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]
