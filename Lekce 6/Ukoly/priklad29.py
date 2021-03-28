"""
Teplota ve městech potřetí
Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech
v listopadu 2017.
Pokud jsi v minulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.
Vyfiltruj si informace o teplotách 13. listopadu 2017.
Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
Vypočti počet dat, které máš pro daný den za jednotlivé regiony.
Vypočti průměrnou teplotu za jednotlivé regiony.
Vypočti maximální a minimální teplotu v každém regionu.
"""
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
teplota = pandas.read_csv("temperature.csv")
import pytemperature
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])
teplota13 = teplota[teplota["Day"]==13]
print(teplota13)
teplota13_bug = teplota13[teplota13["AvgTemperature"]== -99]
teplota13_ocistena = pandas.concat([teplota13, teplota13_bug]).drop_duplicates(keep=False)
print(teplota13_ocistena.groupby(["Region"])["AvgTemperatureCelsia"].count())
print(teplota13_ocistena.groupby(["Region"])["AvgTemperatureCelsia"].mean())
print(teplota13_ocistena.groupby(["Region"]).agg({"AvgTemperatureCelsia":["min", "max"]}))