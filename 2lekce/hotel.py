"""Hotel, Napiš funkci totalPrice, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.
Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. totalPrice(3), totalPrice(2, True)."""

def total_price(persons, breakfast=False):
    cena=persons * 850
    if breakfast:
      cena += persons * 125
    return cena

print(total_price(10, breakfast=True))