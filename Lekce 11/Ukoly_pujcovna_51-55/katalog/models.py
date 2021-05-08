from django.db import models
import datetime
import pytz

class Seznam(models.Model):
  registracni_znacka = models.CharField(max_length=10)
  znacka_a_typ = models.CharField(max_length=100)
  pocet_km = models.IntegerField()
  datum_TK = models.DateField()

  def __str__(self):
    return self.registracni_znacka

  @property
  def technicka(self):
    now = datetime.date.today()
    cas_od_TK = now - self.datum_TK
    return cas_od_TK.days

""" můj původní
  @property
  def technicka(self):
    self.now = datetime.date.today()
    return self.now - self.datum_TK
"""

class Zakaznik(models.Model):
  typy_programu = (
    ("B", "Běžný zákazník"),
    ("Z", "Zlatý program"),
    ("P", "Platinový program"),
  )
  jmeno = models.CharField(max_length=100)
  prijmeni = models.CharField(max_length=100)
  ridicak = models.CharField(max_length=100)
  datum_narozeni = models.DateField()
  program = models.CharField(max_length=1, choices=typy_programu, null=True)

  def __str__(self):
    return self.jmeno.__str__() + " " + self.prijmeni.__str__()

class Vypujcka(models.Model):
  zacatek = models.DateTimeField()
  konec = models.DateTimeField()
  cena = models.IntegerField(null=True)
  auto = models.ForeignKey(Seznam, on_delete=models.SET_NULL, null=True)
  zakaznik = models.ForeignKey(Zakaznik, on_delete=models.SET_NULL, null=True)
  schvaleni = models.BooleanField(default=False)

  @property
  def okamzik(self):
    self.now = datetime.datetime.now()
    self.now = pytz.utc.localize(self.now)
    if self.now > self.konec:
      return("Již uskutečněno.")
    elif self.now >= self.zacatek:
      return("Aktuálně vypůjčeno.")
    elif self.now < self.zacatek:
      return("Bude uskutečněno v budoucnu.")