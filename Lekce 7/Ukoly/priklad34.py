"""
Velikonoce
Ze souboru velikonoce.csv načti data o tom, kolikrát na který datum připadaly Velikonoce v letech 1600 až 2100.
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")
Vytvoř sloupcový graf, který data přehledně zobrazí. Na ose x budou vidět jednotlivá data ("datumy")
a výška sloupce označí, kolikrát na daný den připadly Velikonoce.
Tentokrát jsou popisky a titulek povinné :-)
Po zavolání funkce plot() si výsledek ulož do proměnné ax. Následně zavolej metodu set_ylabel(),
abys nastavila popisek osy y grafu.
ax = velikonoce.plot()
ax.set_ylabel("Počet dnů")
"""

#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")
import pandas
import matplotlib.pyplot as plt
velikonoce = pandas.read_csv("velikonoce.csv")
print(velikonoce.columns)
ax = velikonoce.plot("Datum", "Počet", kind="bar", color="blue")
ax.set_xlabel("Datum")
ax.set_ylabel("Počet")
ax.set_title("Počet Velikonocí v letech 1600 až 2100")
plt.show()

"""
Rozšířené zadání
Vytvoř si datový soubor sama. Můžeš k tomu využít modul dateutil, který při instalaci najdeš pod jménem
python-dateutil. Následně si zkopíruj kód níže a doplň na místo komentářů příkazy, které prováději požadovanou činnost.
import pandas
from dateutil import easter
data = []
for rok in # sem doplň funkci range
  datum = easter.easter(rok)
Naformátuj datum jako řetězec tak, aby obsahovalo jen měsíc a den. Měsíc dej na začátek a za něj den -
použij funkci strftime, kterou jsme spolu probírali
Naformátovaný datum ulož do seznamu data
data = pandas.DataFrame(data, columns=["Datum"])
data = data.groupby("Datum").size()
"""
import pandas
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import easter
data = []
for rok in range(1900,2011):
  datum = easter.easter(rok)
  datum_upravene = datum.strftime("%m-%d")
  data.append(datum_upravene)
#print(data)
data = pandas.DataFrame(data, columns=["Datum"])
data = data.groupby("Datum").size()
print(data)
