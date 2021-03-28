"""
Teplota ve městech
Stáhni si soubor temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.

Pokročilá varianta
Nainstaluj si modul pytemperature a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu
ve stupních Celsia. Ve svém programu nejprve proveď import modulu pytemperature.
Nový sloupec pak přidáš do tabulky tak, že nalevo od = vložíš tabulku a název nového sloupce do hranatých závorek.
Napravo pak můžeš provádět výpočty pomocí již existujících sloupců.
Můžeš např. použít funkci f2c z modulu pytemperature, která převede teplotu ze stupňů Fahrenheita na
stupně Celsia.
import pytemperature
df["AvgTemperatureCelsia"] = pytemperature.f2c(df["AvgTemperature"])
"""
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
teplota = pandas.read_csv('temperature.csv')
#print(teplota.head())
#print(teplota.tail())

#1 Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být?
# Zde je nápověda.
print(teplota[teplota["City"] == "Prague"])

#2 Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
print(teplota[teplota["AvgTemperature"] > 80])

#3 Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu
# (sloupec Region) Evropa (Europe).
print(teplota[(teplota["AvgTemperature"] > 60) & (teplota["Region"] =="Europe")])

#4 Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.
print(teplota[(teplota["AvgTemperature"] > 80) | (teplota["AvgTemperature"] < -20)])

import pytemperature
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])

#5 Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
print(teplota[teplota["AvgTemperatureCelsia"] > 30])

#6 Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno
# v regionu (sloupec Region) Evropa (Europe).
print(teplota[(teplota["AvgTemperatureCelsia"] > 15) & (teplota["Region"] =="Europe")])

#7Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší
# než -10 stupňů. Jsou některé hodnoty podezřelé?
print(teplota[(teplota["AvgTemperatureCelsia"] > 30) | (teplota["AvgTemperatureCelsia"] < -10)])

# Podezřelé jsou extrémní záporné hodnoty v Africe - viz výpis níže, zřejmě špatná data
print(teplota[(teplota["AvgTemperatureCelsia"] < -10) & (teplota["Region"] =="Africa")])