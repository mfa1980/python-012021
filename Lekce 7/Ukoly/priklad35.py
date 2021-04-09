"""
Teplota ve městech popáté
Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech
v listopadu 2017.
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech.
"""
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas
import matplotlib.pyplot as plt
import pytemperature
teplota = pandas.read_csv("temperature.csv")
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])
pomocny = teplota.iloc[:,[3,6]]
helsinki1 = pomocny[pomocny["City"]=="Helsinki"]
helsinki2 = helsinki1["AvgTemperatureCelsia"]
helsinki_seznam = helsinki2.to_numpy().tolist()
miami1 = pomocny[pomocny["City"] == "Miami Beach"]
miami2 = miami1["AvgTemperatureCelsia"]
miami_seznam = miami2.to_numpy().tolist()
tokyo1 = pomocny[pomocny["City"]=="Tokyo"]
tokyo2 = tokyo1["AvgTemperatureCelsia"]
tokyo_seznam = tokyo2.to_numpy().tolist()

tabulka = pandas.DataFrame(helsinki_seznam, columns=["Helsinki"])
tabulka["Miami"] = miami_seznam
tabulka["Tokyo"] = tokyo_seznam
print(tabulka)
tabulka.plot(kind='box', whis=[5, 95])
plt.show()