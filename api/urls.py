from snippets.views import  people
from django.urls import path

urlpatterns = [
    # path("index/", index),
    path("person/", people)
]
