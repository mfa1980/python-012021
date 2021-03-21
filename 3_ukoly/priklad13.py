"""
Vrácení auta
Pokračuj ve své práci pro autopůjčovnu z příkladu 11 a příkladu 12.
Přidej třídě Auto funkci vrat_auto(), která bude mít (krom obligátního self) 2 parametry,
a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal.
Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.
Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden,
a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního
textu a ten vrať pomocí klíčového slova return.
Na konec programu (mimo třídu) přidej dotaz na uživatele, kolik kilometrů zákazník ujel a jak dlouo ho měl půjčené.
Poté vypiš informaci o ceně.
"""
class Auto:
  def __init__(self, registracni_znacka, znacka_typ, kilometry, volne=True):
    self.registracni_znacka = registracni_znacka
    self.znacka_typ = znacka_typ
    self.kilometry = kilometry
    self.volne = volne

  def pujc_auto(self):
    if self.volne:
      return f"Potvrzuji zapůjčení vozidla."
    return f"Vozidlo není k dispozici."

  def get_info(self):
    return f"{self.registracni_znacka}, {self.znacka_typ}"

  def vrat_auto(self, tachometr, dnu):
    self.kilometry = self.kilometry + tachometr
    self.volne = True
    cena = 0
    if dnu <= 7:
      cena = dnu * 400
    else:
      cena = dnu * 300
    return f"Cena za zapůjčení auto činí {cena} Kč."

auto1 = Auto("4A2 3020","Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747","Škoda Octavia", 41253)
uzivatel = str(input("Jaký vůz si chceš zapůjčit - zadej buď Škoda nebo Peugeot: "))
if uzivatel == "Peugeot":
  print(auto1.get_info())
  print(auto1.pujc_auto())
  auto1.volne = False
if uzivatel == "Škoda":
  print (auto2.get_info())
  print(auto2.pujc_auto())
  auto2.volne = False

pocet_kilometru = int(input("Zadej počet najetých kilometrů: "))
pocet_dnu = int(input("Zadej počet dnů zapůjčení vozu: "))
if uzivatel == "Peugeot":
  print(auto1.vrat_auto(pocet_kilometru, pocet_dnu))
  auto1.volne = True
  print(auto1.kilometry)
if uzivatel == "Škoda":
  print(auto2.vrat_auto(pocet_kilometru, pocet_dnu))
  auto2.volne = True
  print(auto2.kilometry)