"""
Hra o trůny
Stáhni si soubor character-deaths.csv, který obsahuje informace o smrti některých postav z prvních pěti
knih románové série Píseň ohně a ledu (A Song of Fire and Ice).
"""
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

#1 Načti soubor do tabulky (DataFrame) a nastav sloupec Name jako index.
import pandas
postavy = pandas.read_csv("character-deaths.csv")
postavy = postavy.set_index("Name")

#2 Zobraz si sloupce, které tabulka má. Posledních pět sloupců tvoří zkratky názvů knih a informace o tom,
# jestli se v knize postava vyskytuje.
print(postavy.columns)

#3 Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali".
pomocne = postavy.loc[:,"Death Year"]
print(pomocne["Hali"])

#4 Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".
print(postavy.loc["Gevin Harlaw":"Gillam"])

#5 Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year.
print(postavy.loc["Gevin Harlaw":"Gillam", "Death Year"])

#6 Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom, v jakých knihách
# se postava vyskytuje, tj. vypiš všechny sloupce mezi GoT a DwD.
print(postavy.loc["Gevin Harlaw":"Gillam","GoT":"DwD"])