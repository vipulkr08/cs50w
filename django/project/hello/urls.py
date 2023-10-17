from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("vipul/", views.vipul, name="vipul"),
    path("vishal/", views.vishal, name="vishal")
]