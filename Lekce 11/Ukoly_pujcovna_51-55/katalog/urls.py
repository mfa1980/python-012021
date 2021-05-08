from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="katalog"),
    path("seznam/", views.SeznamView.as_view(), name="seznam"),
    path("vypujcka/", views.VypujckaView.as_view(), name="vypujcka"),
    path("zakaznik/", views.ZakaznikView.as_view(), name="zakaznik"),
    path("<int:pk>vypujcka/", views.DetailVypujckaView.as_view(), name="vypujcka_detail"),
    path("<int:pk>zakaznik/", views.DetailZakaznikView.as_view(), name="zakaznik_detail"),
    path("<int:pk>seznam/", views.DetailSeznamView.as_view(), name="seznam_detail"),
    path("zadejAuto/", views.ZadejAuto.as_view(), name="seznam_pridat"),
    path("zadejVypujcku/", views.ZadejVypujcku.as_view(), name="vypujcka_pridat"),
    path("zadejZakaznika/", views.ZadejZakaznika.as_view(), name="zadej_zakaznika"),
    ]