from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from . import models

"""
<--Toto je původní třída SeznamView s funkcí get()-->
class SeznamView(View):
  def get(self, request):
    return HttpResponse("Zde bude seznam aut.")
"""

class IndexView(TemplateView):
  template_name = "katalog/base.html"

class SeznamView(ListView):
  model = models.Seznam
  template_name = "katalog/seznam_list.html"

class DetailSeznamView(DetailView):
  model = models.Seznam
  template_name = "katalog/seznam_detail.html"

class VypujckaView(ListView):
  model = models.Vypujcka
  template_name = "katalog/vypujcka_list.html"

class DetailVypujckaView(DetailView):
  model = models.Vypujcka
  template_name = "katalog/vypujcka_detail.html"

class ZakaznikView(ListView):
  model = models.Zakaznik
  template_name = "katalog/zakaznik_list.html"

class DetailZakaznikView (DetailView):
  model = models.Zakaznik
  template_name = "katalog/zakaznik_detail.html"

class ZadejAuto(CreateView):
  model = models.Seznam
  template_name = "katalog/pridat_auto.html"
  fields = ["registracni_znacka", "znacka_a_typ", "pocet_km", "datum_TK"]
  success_url = reverse_lazy('seznam')

class ZadejVypujcku(CreateView):
  model = models.Vypujcka
  template_name = "katalog/pridat_vypujcka.html"
  fields = ["zacatek", "konec", "cena", "auto", "zakaznik"]
  success_url = reverse_lazy('vypujcka')

class ZadejZakaznika(CreateView):
  model = models.Zakaznik
  template_name =  "katalog/pridat_zakaznik.html"
  fields = ["jmeno", "prijmeni", "ridicak", "datum_narozeni"]
  success_url = reverse_lazy('vypujcka_pridat')