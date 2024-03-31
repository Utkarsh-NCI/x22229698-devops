from django.http import Http404
from django.shortcuts import render,redirect
from modules.models import Topic,Module
from .forms import FeedbackForm

def index(request):
    module = Module.objects.all()
    context = {'modules': module}
    return render(request, 'modules/index.html', context)
    
def show(request, module_id):
    try:
        module = Module.objects.get(pk=module_id)
    except Module.DoesNotExist:
        raise Http404("Module does not exist")
    topics =module.topic_set.all()
    context = {
        'module':module,
        'topics':topics,
    }    
    return render(request, 'modules/module.html', context)    

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')        
    else:
        print("GET")
        form = FeedbackForm()
    return render(request, 'modules/feedback.html', {'form': form})