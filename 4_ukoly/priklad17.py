"""
Streamovací služba podruhé
Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají.
Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani, který udává celkovou délku pořadů,
které uživatel zhlédl. Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.
Třídám Serial a Film přidej funkce get_celkova_delka(), která vrátí celkovou délku filmu/seriálu
(u seriálu je to počet episod násobený délkou jedné episody).
Třídě Uzivatel přidej funkci pripocti_zhlednuti(), která bude mít jeden parametr. Funkce zvýší atribut
udávající celkovou délku sledávní o zadaný parametr.
Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci, že uživatel zhlédne
film a seriál, které jsi vytvořil(a) jako objekty. Uživateli připočti délky děl k délce sledování,
využij k tomu funkci get_celkova_delka() u objektu a seriálu, abys zjistil(a), kolik minut (nebo hodin)
videa celkem uživatel zhlédl.
Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné a
tuto pomocnou proměnnou potom předáš jako parametr funkci pripocti_zhlednuti().
Složitější varianta
V pokročilejší variantě neeviduj pouze délku sledování ale i to, jaké pořady uživatel sledoval.
Namísto délky sledování vytvoř atribut, který bude udávat zhlédnuté pořady (ideální pro tento účel je seznam).
Dále přidej funkci zhledni_polozku(), která do seznamu zhlédnutých pořadů přidánovou položku.
Dále vytvoř funkci delka_sledování() pro uživatele, která projde položky v seznamu a vrátí celkovou délku
všech pořadů, které uživatel zhlédl.
Vytvoř si ukázkové objekty a ověř, že vše funguje.
"""
class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr
  def get_info(self):
    return f"Název: {self.nazev}, žánr: {self.zanr}"

class Film(Polozka):
  def __init__(self, nazev, zanr, delka):
    super().__init__(nazev, zanr)
    self.delka = delka
  def get_info(self):
    return super().get_info() + f", délka: {self.delka}"
  def get_celkova_delka(self):
    celkova_celka = self.delka
    return celkova_celka

class Serial(Polozka):
  def __init__(self, nazev, zanr, pocet_epizod, delka_epizody):
    super().__init__(nazev, zanr)
    self.pocet_epizod = pocet_epizod
    self.delka_epizody = delka_epizody
  def get_info(self):
    return super().get_info() + f", počet epizod: {self.pocet_epizod}, délka epizody: {self.delka_epizody}"
  def get_celkova_delka(self):
    celkova_celka = self.pocet_epizod * self.delka_epizody
    return celkova_celka

class Uzivatel:
  def __init__(self, uzivatelske_jmeno):
    self.uzivatelske_jmeno = uzivatelske_jmeno
    self.delka_sledovani = 0
  def pripocti_zhlednuti(self, delka):
    self.delka_sledovani += delka
    #print(self.delka_sledovani)

serial1 = Serial("Twin Peaks", "fantasy", 10, 60)
film1 = Film("Na samotě u lesa", "komedie", 90)
uzivatel1 = Uzivatel("Petr")
#print(film1.get_info())
#print(serial1.get_info())
#print(serial1.get_celkova_delka())
#print(film1.get_celkova_delka())
uzivatel1.pripocti_zhlednuti(serial1.get_celkova_delka())
uzivatel1.pripocti_zhlednuti(film1.get_celkova_delka())
print(f"Uživatel {uzivatel1.uzivatelske_jmeno} celkem viděl {uzivatel1.delka_sledovani} minut záznamu.")
