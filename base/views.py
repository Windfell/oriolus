from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime


def about(request):
    return render_to_response('about.html')


def index(request):
    return render_to_response('base.html')


def current_time(request):
    now = datetime.datetime.now()
    time_str = str(now).split('.')[0]
    return render_to_response('lab/current_datetime.html', {'current_date': time_str})

