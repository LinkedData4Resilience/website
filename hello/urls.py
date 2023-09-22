from django.urls import path

from . import views

app_name = "hello"

urlpatterns = [
    path("", views.index, name="index"),
    path("data/", views.data, name="data"),
    path("data/integrated", views.integrated, name="integrated"),
    path("data/integrated/April2023/event/<eventid>", views.integratedevent, name="integratedevent"),

    path("data/EOR", views.EOR, name="EOR"),
    path("data/EOR/April2023", views.EOR, name="EOR"),
    path('data/EOR/April2023/event/<eventid>', views.EORevent, name='EORevent'),

    path("data/CH/", views.CH, name="CH"),
    path("data/CH/April2023/", views.CH, name="CH"),
    path('data/CH/April2023/event/<eventid>', views.CHevent, name='CHevent'),

    path("publication/", views.publication, name="publication"),
]
