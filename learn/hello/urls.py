from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Joe", views.Joe, name="Joe"),
    path("<str:names>", views.greet, name="greet"),

]