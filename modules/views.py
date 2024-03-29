from django.http import Http404
from django.shortcuts import render
from modules.models import Topic,Module

def index(request):
    module = Module.objects.all()
    context = {'modules': module}
    return render(request, 'modules/index.html', context)
    
def show(request, module_id):
    try:
        module = Module.objects.get(pk=module_id)
    except Module.DoesNotExist:
        raise Http404("Module does not exist")
    print(module.topic_set.all())    
    context = {'module':module}
    return render(request, 'modules/module.html', context)    