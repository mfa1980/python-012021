"""
Pokročilejší varianta
Podívej se do dokumentace k modulu forex-python. Zjistíš, že umí pár dalších zajímavých věcí, například převod měny
do Bitcoinu. Zkus pomocí modulu vytvořit program, který se zeptá uživatele na měnu a požadovaný počet Bitcoinů
a vrátí mu množství měny, které by potřeboval, aby požadované množství Bitcoinů mohl koupit.
"""
from forex_python.bitcoin import BtcConverter
pozadovana_mena = input("Zadej zkratku měny: ")
pocet_bitcoin = int(input("Zadej počet Bicoinů: "))
cena_bitcoin = 0
castka = 0
b = BtcConverter()
cena_bitcoin = b.get_latest_price(pozadovana_mena)
print(f"Cena za 1 bitcoin: {cena_bitcoin} {pozadovana_mena}.")
castka = pocet_bitcoin * cena_bitcoin
print(f"Cena za {pocet_bitcoin} bitcoin: {castka} {pozadovana_mena}.")