from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Module, Lesson

# Create your views here.
def index(request):
    return render(request, "modules/index.html", {
        "modules": Module.objects.all()
    })


def module(request, module_id):
    try:
        module = Module.objects.get(id=module_id)
    except Module.DoesNotExist:
        raise Http404("Module not found.")
    return render(request, "modules/module.html", {
        "module": module,
        "lessons": module.lessons.all(),
        "non_lessons": Lesson.objects.exclude(modules=module).all()
    })
