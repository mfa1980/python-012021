"""
Detektivky podruhé
Vraťme se k software pro našeho nakladatele. Nakladatel má nyní v software dva slovníky,
které obsahují informace o prodejích knih v letech 2019 a 2020.
Uvažuj, že uživatel se zajímá o prodeje konkrétní knihy. Zeptej se uživatele na název knihy
a poté vypiš informaci o tom, kolik se této knihy celkem prodalo. Nezapomeň na to, že některé knihy
byly prodávány pouze v jednom roce.
"""
prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}
nazev = input("Zadej název knihy: ")
pocet2019 = 0
pocet2020 = 0
if nazev in prodeje2019:
  pocet2019 = prodeje2019[nazev]
if nazev in prodeje2020:
  pocet2020 = prodeje2020[nazev]
print(f"Celkový počet prodaných knih je {pocet2019+pocet2020}")

# V roce 2020 je kniha "Zkus mě chytit" uvedena 2x.