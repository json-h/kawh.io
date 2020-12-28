from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def import_league(request):
    return render(request, 'main/import_league.html')