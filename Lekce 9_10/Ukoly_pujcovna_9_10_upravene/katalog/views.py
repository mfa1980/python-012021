from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic import ListView
from . import models

"""
původní class IntexView(View):
"""

class IndexView(TemplateView):
  template_name = "katalog/base.html"
  def get(self, request):
    return HttpResponse("<h1>Vítejte v naší autopůjčovně!</h1>"
                        "<h2>Důležité odkazy</h1>"
                        "<a href='http://localhost:8000/katalog/seznam/'>Seznam vozů</a><br>"
                        "<a href='http://localhost:8000/katalog/vypujcka/'>Seznam zápůjček</a><br>"
                        "<a href='http://localhost:8000/katalog/zakaznik/'>Seznam zákazníků</a><br>"
                        "<h2>O naší autopůjčovně</h2>"
                        "<p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>"
                        "<h2>Nabízené služby</h2>"
                        "<ul>"
                        "<li>Půjčovna osobních automobilů</li>"
                        "<li>Půjčovna přívěsných vozíků</li>"
                        "<li>Půjčovna obytných přívěsů</li>"
                        "</ul>")

"""
class SeznamView(View):
  def get(self, request):
    return HttpResponse("Zde bude seznam aut.")
"""

class SeznamView(ListView):
    model = models.Seznam
    template_name = "katalog/seznam_list.html"

class VypujckaView(ListView):
    model = models.Vypujcka
    template_name = "katalog/vypujcka_list.html"

class ZakaznikView(ListView):
  model = models.Zakaznik
  template_name = "katalog/zakaznik_list.html"