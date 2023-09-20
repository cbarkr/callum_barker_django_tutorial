from django.urls import path, URLPattern
from . import views

app_name = "organization"

urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detail, name="detail"),
]
