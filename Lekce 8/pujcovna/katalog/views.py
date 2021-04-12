from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class IndexView(View):
  def get(self, request):
    return HttpResponse("<h1>Vítejte v naší autopůjčovně!</h1>"
                        "<a href='http://localhost:8000/katalog/seznam/'>Jaká auta máme?</a><br>"
                        "<h2>O naší autopůjčovně</h2>"
                        "<p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>"
                        "<h2>Nabízené služby</h2>"
                        "<ul>"
                        "<li>Půjčovna osobních automobilů</li>"
                        "<li>Půjčovna přívěsných vozíků</li>"
                        "<li>Půjčovna obytných přívěsů</li>"
                        "</ul>")

class SeznamView(View):
  def get(self, request):
    return HttpResponse("Zde bude seznam aut.")
