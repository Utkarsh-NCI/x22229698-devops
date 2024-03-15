from django.http import Http404
from django.shortcuts import render
from .models import Topic
def index(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'modules/index.html', context)