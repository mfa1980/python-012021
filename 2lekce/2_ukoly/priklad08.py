"""
SMS brána
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program,
který provede následující činnosti:
- Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
- Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

Tvůj program bude obsahovat dvě funkce:
- První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné
(pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné.
Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
- Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla.
Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a
pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

Tip: Zkus svoji první funkci vytunit tak, že si bude umět poradit s mezerami v telefonním čísle.
Mezer se zbavíš tak, že použiješ funkci replace() a tečkovou notaci.
První parametr je znak, který chceš nahradit, a druhý parametr nový znak. Níže je příklad použití.

tel_cislo = "+420 734 123 456"
tel_cislo = tel_cislo.replace(" ", "")
"""

def funkce1(tel_cislo):
  tel_cislo = tel_cislo.replace(" ", "")
  if len(tel_cislo) == 13 or len(tel_cislo) == 9:
    return 1
    #print(f"Číslo je správné.")
  else:
    print(f"Telefonní číslo bylo zadáno ve špatném formátu.")
    return 0

def funkce2(zprava):
  cena = 0
  delka_zpravy = len(zprava)
  if delka_zpravy % 180 == 0:
    cena = 3 * (delka_zpravy // 180)
  else:
    cena = 3 + 3 * (delka_zpravy // 180)
  print(f"Cena SMS zprávy je {cena},-Kč.")

tel_cislo = input("Zadej telefonní číslo: ")
if funkce1(tel_cislo):
  zprava = input("Napiš zprávu: ")
  funkce2(zprava)
