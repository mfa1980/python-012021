from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="katalog"),
    path("seznam/", views.SeznamView.as_view(), name="seznam"),
    path("vypujcka/", views.VypujckaView.as_view(), name="vypujcka"),
    path("zakaznik/", views.ZakaznikView.as_view(), name="zakaznik")
]