"""
Instalace modulu
Zopakuj si postup při instalaci modulu. Pojďme si vytvořit směnárnu, která nemá kurzy zadané pevně,
ale umí si kurz měny stáhnout z internetu.
V PyCharmu klikni na File -> Settings -> Project -> Python Interpreter. Následně klikni na tlačítko +
(Install) a vyhledej modul forex-python. Dále klini na Install Package a potvrď instalaci.
Dále se podívej na následující příklad, jak s modulem pracovat. Na prvním řádku je import, aby Python věděl,
že s modulem chceme pracovat. Na druhém řádku vytvoříme objekt prevodnik (je to objekt třídy CurrencyRates),
který se stará o převod měn.
Uvažujme třeba, že chceme spočítat, kolik by nás stálo, pokud bychom chtěli 10 dolarů.
Použijeme funkci convert(), která má jako první parametr zkraktu cílové měny, jako druhé parametr zkratku
zdrojové měny a jako třetí parametr množství požadovaných dolarů. Funkce vypočte, kolik jednotek zdrojové
měny je potřeba zaplatit, aby to odpovídalo požadovanému množství cílové měny.
Zkus program upravit tak, aby zjistil požadovanou měnu od uživatele (pomocí funkce input()).
Uvažuj, zkus např. pracovat s měnami EUR, GBP nebo DKK. Následně od uživatele získej i požadované množství
cílové měny. Nezapomeň toho množství převést na typ int.
"""
from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("Zadej částku v cílové měně USD: "))
cena_v_korunach = prevodnik.convert('USD', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)

from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("Zadej částku v cílové měně EUR: "))
cena_v_korunach = prevodnik.convert('EUR', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)

from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("Zadej částku v cílové měně DKK: "))
cena_v_korunach = prevodnik.convert('DKK', 'CZK', pozadovano_v_cilove_mene)
print(cena_v_korunach)

# alternativní pojetí od Lídy (bez zadání hodnoty od uživatele:
from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
print(f"100 USD = {prevodnik.convert('USD', 'CZK', 100)} CZK")
print(f"100 EUR = {prevodnik.convert('EUR', 'CZK', 100)} CZK")
print(f"100 DKK = {prevodnik.convert('DKK', 'CZK', 100)} CZK")
