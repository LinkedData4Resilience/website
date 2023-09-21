from django.urls import path

from . import views

app_name = "hello"

urlpatterns = [
    path("", views.index, name="index"),
    path("data/", views.data, name="data"),
    path("publication/", views.publication, name="publication"),
]
