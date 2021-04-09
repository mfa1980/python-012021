"""
Twilio podruhé
Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020.
Soubor obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.
Stažení souboru pomocí wget:
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
import pandas
import matplotlib.pyplot as plt
twilio = pandas.read_csv("twlo.csv")
Výše uvedeným programem načti data o vývoji ceny akcie. Vytvoř čárový graf vývoje zavírací ceny akcie (sloupec Close)
v čase. Zkus nyní převést sloupec Date na typ datetime příkazem níže a vytvoř stejný graf jako předtím.
Porovnej grafy a zjisti, co se změnilo.
twilio["Date"] = pandas.to_datetime(twilio["Date"])
"""

#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
import pandas
import matplotlib.pyplot as plt
import datetime
twilio = pandas.read_csv("twlo.csv")
twilio.plot("Date", "Close")
plt.show()
twilio["Date"] = pandas.to_datetime(twilio["Date"])
twilio.plot("Date", "Close")
plt.show()
# po převodu na datetime přehlednější hodnoty na ose x

"""
Dobrovolný doplněk
Přidej ke grafům popisky os a titulky. Po zavolání funkce plot() si výsledek ulož do proměnné ax.
Následně zavolej metodu set_ylabel(), abys nastavila popisek osy y grafu.
ax = twilio.plot()
ax.set_ylabel("Cena v dolarech")
Obdobně využij metody set_title() a set_xlabel() a nastav popisek osy x a titulek grafu.
"""
ax = twilio.plot("Date", "Close")
ax.set_xlabel("Datum")
ax.set_ylabel("Cena v dolarech")
ax.set_title("Uzavírací cena akcií Twilio")
plt.show()