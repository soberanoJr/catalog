from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:module_id>", views.module, name="module"),
]