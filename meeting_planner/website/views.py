from datetime import datetime
from time import strftime
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meetings

def welcome(request):
    return render(request, "webiste/welcome.html", {'meetings': Meetings.objects.all()})

def date(request):
    return HttpResponse("The current time is: "+ str(datetime.now()))

def about(request):
    return HttpResponse("I am django developer")
