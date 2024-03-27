from django.http import Http404
from django.shortcuts import render
from modules.models import Topic,Module

def index(request):
    module = Module.objects.all()
    context = {'modules': module}
    return render(request, 'modules/index.html', context)