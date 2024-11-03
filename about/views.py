from django.shortcuts import render
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView


def CV(request):
    return HttpResponseRedirect("/static/CV.pdf")

class games(TemplateView):
    template_name = "video_games.html"
