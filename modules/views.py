from django.http import Http404
from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Module

# Create your views here.
def index(request):
    return render(request, "modules/index.html", {
        "modules": Module.objects.all().order_by("id")
    })

def module(request, module_id):
    try:
        module = Module.objects.get(id=module_id)
    except Module.DoesNotExist:
        raise Http404("Module not found.")
    return render(request, "modules/module.html", {
        "module": module,
        "lessons": module.lessons.all().order_by("name")
    })

