from django.urls import path, URLPattern
from . import views

app_name = "organization"

urlpatterns: list[URLPattern] = [
    path("", views.IndexView.as_view(), name="index"),
]
