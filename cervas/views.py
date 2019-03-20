from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . import urls

# Create your views here.

def index(request):
    return HttpResponse("Hello world")


def markets_list(request):
    return render(request, 'cervas/market_list.html', {})
