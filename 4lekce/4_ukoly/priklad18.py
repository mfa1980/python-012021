"""
Inverview
Uvažuj následující třídu Kontakt, která slouží k evidenci všech kontaktů (např. zákazníků, zaměstnanců,
uchazečů o práci atd.).
class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email
Vytvoř třídu Uchazec, která bude dědit od třídy Kontakt a která reprezentuje uchazeče o práci.
Uchazeč o práci bude mít navíc atribut datum_pohovoru a zapis_z_pohovoru. Datum pohovoru objekt získá z parametru
a zápis z pohovoru je na začátku prázdný řetězec "".
Dále přidej funkci uloz_zapis(), která bude mít jako parametr textový zápis pohovoru.
Tato funkce ohlídá, zda uživatel omylem nezadává zápis k pohovoru, který ještě neproběhl.
Na začátku funkce porovnej aktuální datum a datum pohovoru. Pokud podle data pohovor ještě neproběhl,
vrať chybový text, který informuje uživatele o chybě. Pokud již podle data pohovor proběhl, ulož zápis
a vrať text s informací, že zápis byl uložen.
"""
from datetime import datetime, timedelta
class Kontakt:

  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec(Kontakt):
  def __init__ (self, jmeno, email, datum_pohovoru):
    super().__init__(jmeno, email)
    self.datum_pohovoru = datum_pohovoru
    self.zapis_z_pohorovu = ""

  def uloz_zapis (self,zapis):
    self.datum_pohovoru = datetime.strptime(self.datum_pohovoru,"%Y-%m-%d")
    if datetime.now() <= self.datum_pohovoru:
      return f"Pohovor ještě neproběhl."
    else:
      self.zapis_z_pohorovu = zapis
      return f"Zápis z pohovoru byl uložen."

uchazec1 = Uchazec("Karel Vomáčka", "karel@vomacka.cz", "2021-02-03")
uchazec2 = Uchazec("Petra Nováková", "petra@seznam.cz", "2021-11-03")
print (uchazec1.uloz_zapis("Bylo to super."))
print (f"{uchazec1.jmeno}, {uchazec1.email}, {uchazec1.datum_pohovoru}, {uchazec1.zapis_z_pohorovu}")
print (uchazec2.uloz_zapis("???"))
print (f"{uchazec2.jmeno}, {uchazec2.email}, {uchazec2.datum_pohovoru}, {uchazec2.zapis_z_pohorovu}")