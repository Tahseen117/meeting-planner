from django import http
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from .models import Meetings, Room
from django.forms import modelform_factory


def details(request, id):
    meeting = get_object_or_404 ( Meetings, pk=id)
    return render(request, "meetings/details.html", {'meeting': meeting})

def room_list(request):
    return render (request, "meetings/rooms.html", {'rooms': Room.objects.all()})

MeetingForm = modelform_factory(Meetings, exclude=[]) 
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {'form':form})
