"""
Řazení
Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech
v listopadu 2017.
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
Pokud jsi v předminulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.

Vyfiltruj si informace o teplotách 13. listopadu 2017.
Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
Seřad hodnoty v souboru podle teploty od největší po nejmenší.
Vypiš pět měst s nejvyšší teplotou a pět měst s nejnižší teplotou.
"""
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas
teplota = pandas.read_csv("temperature.csv")
import pytemperature
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])
teplota13 = teplota[teplota["Day"]==13]
teplota13_bug = teplota13[teplota13["AvgTemperature"]== -99]
teplota13_ocistena = pandas.concat([teplota13, teplota13_bug]).drop_duplicates(keep=False)
print(teplota13_ocistena.sort_values(by="AvgTemperatureCelsia", ascending=False))
#print(teplota13_ocistena.sort_values(by="AvgTemperatureCelsia", ascending=False).head(5))
print(teplota13_ocistena.sort_values(by="AvgTemperatureCelsia", ascending=False).iloc[:5,3])
#print(teplota13_ocistena.sort_values(by="AvgTemperatureCelsia", ascending=False).tail(5))
print(teplota13_ocistena.sort_values(by="AvgTemperatureCelsia", ascending=False).iloc[-5:,3])
