"""
Histogram platů
Stáhni si znovu soubor platy_2021_02.csv s informacemi o platech v softwarové firmě, se kterými jsme již pracovali
v příkladu 26.
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
Načti si tato data do tabulky a vytvoř histogram. Nastav vhodně hranice skupin histogramu (parametr bins),
aby byl graf přehledný a snadno interpretovatelný.
Dobrovolný doplněk
Vyzkoušej si vytvořit podgrafy. pandas a matplotlib to umí poměrně jednoduše a to pomocí parametru by metody hist().
Jako parametr vlož sloupec, podle kterého chceš data do podgrafů rozdělit. Musíš vložit sloupec ve formě dat,
nikoli pouze jeho název.
Vytvoř pro zadaná data podgrafy pro jednotlivá města. Načti si informace o městě, ve kterém jednotliví pracovníci
pracují (to jsme již dělali v příkladu) příkladu 26. Následně sloupec mesto použij na rozdělení podgrafů.
"""
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")

#základní zadání
import pandas
import matplotlib.pyplot as plt
platy = pandas.read_csv("platy_2021_02.csv").dropna()
platy["plat"].hist(bins=[30000,32000,34000,36000,38000,40000,42000,44000,46000,48000,50000,52000,54000,56000,58000,60000])
plt.show()

# doplněk
import pandas
praha = pandas.read_csv("zam_praha.csv").dropna()
plzen = pandas.read_csv("zam_plzeň.csv").dropna()
liberec = pandas.read_csv("zam_liberec.csv").dropna()
praha["mesto"] = "Praha"
plzen["mesto"] = "Plzeň"
liberec["mesto"] = "Liberec"
zamestnanci = pandas.concat([praha,plzen,liberec], ignore_index = True)
platy_se_jmeny = pandas.merge(zamestnanci, platy)
print(platy_se_jmeny.shape)
print(platy_se_jmeny.columns)
platy_se_jmeny[["mesto","plat"]].hist(by=["mesto"], bins=[30000,35000,40000,45000,50000,55000,60000])
plt.show()