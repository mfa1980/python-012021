"""Pokročilejší varianta
Uvažujme nyní společnost, která přepravuje balíky do více zemí. V dokumentaci si najdi odstavec Localization.
Tam najdeš informaci, že "faker.Faker also supports multiple locales". Podívej se, jak je v příkladu vytvořen
objekt Faker (je použit seznam). Zkus nyní upravit svůj program tak, aby generoval adresy v rámci České i
Slovenské republiky. Příslušnou zkratku pro Slovensko najdeš taktéž v dokumentaci k modulu."""

from faker import Faker
generator_falesnych_dat = Faker(["cs_CZ", "sk_SK"])
#print(generator_falesnych_dat.name())
#print(generator_falesnych_dat.address())

class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print("Balík doručte na adresu: " + self.address)

  def __init__(self, name, address):
    self.name = name
    self.address = address

balik1 = Balik(generator_falesnych_dat.name(), generator_falesnych_dat.address())
print(balik1.get_info())