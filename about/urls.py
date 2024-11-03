from django.urls import path
from . import views

urlpatterns = [
    path("CV", views.CV, name="CV"),
    path("games", views.games.as_view(), name="games"),
]
