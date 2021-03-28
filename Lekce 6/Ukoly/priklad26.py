"""
Zaměstnanci
Uvažuj, že zpracováváš analýzu pro softwarovou firmu. Firma má kanceláře v Praze, Plzni a Liberci.
Seznam zaměstnanců pro jednotlivé kanceláře najdeš v souborech zam_praha.csv, zam_plzeň.csv a zam_liberec.csv.
Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový sloupec mesto,
které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join)
s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.
Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor,
znamená to, že v naší firmě již nepracuje.
Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.
Dobrovolný doplněk
Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují.
Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují.
Tabulku ulož do souboru CSV.
"""
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

import pandas
praha = pandas.read_csv("zam_praha.csv").dropna()
plzen = pandas.read_csv("zam_plzeň.csv").dropna()
liberec = pandas.read_csv("zam_liberec.csv").dropna()
praha["mesto"] = "Praha"
plzen["mesto"] = "Plzeň"
liberec["mesto"] = "Liberec"
zamestnanci = pandas.concat([praha,plzen,liberec], ignore_index = True)
platy = pandas.read_csv("platy_2021_02.csv").dropna()
platy_se_jmeny = pandas.merge(zamestnanci, platy)
print(f"Počet řádků/slouců tabulky zaměstnanci: {zamestnanci.shape}")
print(f"Počet řádků/slouců tabulky platy: {platy.shape}")
print(f"Počet řádků/slouců tabulky platy se jmény: {platy_se_jmeny.shape}")
print(platy_se_jmeny.groupby("mesto")["plat"].mean())
nepracuji_pomocny = pandas.merge(zamestnanci,platy,how = "left")
nepracuji = nepracuji_pomocny[nepracuji_pomocny["plat"].isnull()]
nepracuji_jmena = nepracuji.iloc[:,[0,1]]
nepracuji_jmena.to_csv("nepracuji_jmena.csv", index=False)