"""
Pokračuj ve své práci pro autopůjčovnu, kterou jsi začala v příkladu 11.
Třídě Auto přidej funkci pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr.
Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu, který určuje,
zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text
"Vozidlo není k dispozici".
Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle
(stačí registrační značka a značka a typ vozidla) jako řetězec.
Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit.
Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci
o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto.
Dotaz na uživatele a výpis výsledků si v programu zkopíruj, abys dokázala otestovat,
že funkce nedovolí půjčit stejné auto dvakrát.
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

uzivatel = str(input("Jaký vůz si chceš zapůjčit - zadej buď Škoda nebo Peugeot: "))
if uzivatel == "Peugeot":
  print(auto1.get_info())
  print(auto1.pujc_auto())
  auto1.volne = False
if uzivatel == "Škoda":
  print (auto2.get_info())
  print(auto2.pujc_auto())
  auto2.volne = False