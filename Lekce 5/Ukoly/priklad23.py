"""
Vakcíny
Stáhni si soubor country_vaccinations.csv o průběhu očkování proti nemoci COVID-19.
"""
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")

#1 Dotaz na počty očkovaných (sloupec total_vaccinations) v jednotlivých státech dne 2021-03-10 (s datem pracuj
# úplně stejně jako s řetězcem, tj. nevyužívej modeul datetime, ale vlož do dotazu přímo řetězec).

import pandas
vakciny = pandas.read_csv("country_vaccinations.csv")
denni = vakciny[vakciny["date"] == "2021-03-10"]
print(denni[["country","total_vaccinations"]])

#2 Dotaz na řádky, kde 2021-03-10 bylo naočkováno více než 1 mil. obyvatel.
pomocne = vakciny[(vakciny["date"] == "2021-03-10") & (vakciny["daily_vaccinations"] > 1_000_000)]
print(pomocne)

#3 Podíváme se na extrémní hodnoty. Napiš dotaz na řádky, kde za daný den naočkování více než 100 tisíc lidí
# nebo naopak méně než 100 lidí.
extrem_max = vakciny[(vakciny["daily_vaccinations"] > 100_000) & (vakciny["date"] == "2021-03-10")]
extrem_min = vakciny[(vakciny["daily_vaccinations"] < 100) & (vakciny["date"] == "2021-03-10")]
print(extrem_max)
print(extrem_min)

#4 dobrovolné: Vypiš informace o očkování za dny 2021-03-10 a 2021-03-11 pro státy United Kingdom, Finland a
# Italy. Použij např. funkci isin().
vypocet = vakciny[(vakciny["date"].isin(["2021-03-10", "2021-03-11"])) & (vakciny["country"].isin(["United Kingdom", "Finland", "Italy"]))]
print(vypocet)

#5 dobrovolné: Vypiš informace o očkování pro Japan mezi daty 2021-03-03 a 2021-03-09. Data v tomto
# formátu můžeš porovnávat pomocí operátorů >= a <= jako řetězce, tj. opět nemusíš použít modul datetime.
vypocet2 = vakciny[(vakciny["date"] >= "2021-03-03") & (vakciny["date"] <= "2021-03-09") & (vakciny["country"] == "Japan")]
print(vypocet2)