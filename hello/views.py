from django.shortcuts import render

from .models import Greeting

# Create your views here.


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Welcome to the webiste of the Linked4Resilience project.\nThis website will be updated soon.")

#
# def db(request):
#     # If you encounter errors visiting the `/db/` page on the example app, check that:
#     #
#     # When running the app on Heroku:
#     #   1. You have added the Postgres database to your app.
#     #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
#     #      process entry in `Procfile`, git committed your changes and re-deployed the app.
#     #
#     # When running the app locally:
#     #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.
#
#     greeting = Greeting()
#     greeting.save()
#
#     greetings = Greeting.objects.all()
#
#     return render(request, "db.html", {"greetings": greetings})
