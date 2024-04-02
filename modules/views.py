"""Module application views"""
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET,require_http_methods
from modules.models import Module
from .forms import FeedbackForm


@require_GET
def index(request):
    """Landing page"""
    module = Module.objects.all() # pylint: disable=no-member
    context = {"modules": module}
    return render(request, "modules/index.html", context)

@require_GET
def show(request, module_id):
    """Specific module description"""
    try:
        module = Module.objects.get(pk=module_id) # pylint: disable=no-member
    except Exception as exc:
        raise Http404("Module does not exist") from exc
    topics = module.topic_set.all()
    context = {
        "module": module,
        "topics": topics,
    }
    return render(request, "modules/module.html", context)

@require_http_methods(["GET", "POST"])
def feedback(request):
    """Feedback form for modules"""
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = FeedbackForm()
    return render(request, "modules/feedback.html", {"form": form})
    