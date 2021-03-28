"""
Twilio
Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020.
Soubor obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.
"""
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
twilio = pandas.read_csv("twlo.csv")

#1 Zjisti, kolik má soubor řádek a kolik sloupců.
print(twilio.shape)
# počet řádků print(twilio.shape([0])) - není vyzkoušené

#2 Podívej se na 5 řádků s cenami na začátku souboru, využij k tomu funkci iloc i funkci head().
print(twilio.head())
print(twilio.iloc[:5])

#3 U akcií nás zajímají především nejnovější ceny. Podívej se na poslední řádek souboru.
print(twilio.iloc[-1])
print(twilio.tail())

#4 Počet řádků ulož do proměnné pocet_radku jako číslo.
pocet_radku = len(twilio)

#5 Pokud funkci iloc zadáš číslo řádku i číslo sloupce, odkazuješ se na jednu konkrétní hodnotu.
# Pandas ti tuto hodnotu vrací jako číslo. Načti si tedy první hodnotu zavírací ceny (sloupec Close)
# v souboru a poslední hodnotu zavírací ceny v souboru. Vypočítej, o kolik procent se zvýšila hodnota akcie.
prvni = twilio.iloc[0, 5]
posledni = twilio.iloc[pocet_radku-1, 5]
zmena = (posledni-prvni)/prvni * 100
print(f"Cena akcie je změnila o {zmena} %.")

#6 Vyber si sloupec s maximální cenou akcie (sloupec High) za jednotlivé dny pomocí loc nebo iloc jako sérii.
# Na sloupec použij funkci .max(), abys zjistila maximální zaznamenanou cenu akcie za celé období.
# Obdobným způsobem použij funkci .min() na sloupec Low. Z těchto hodnot zjistíš maximální rozsah obchodní
# ceny akcie, což je základ jednoho z akciových ukazatelů (price range).
nejvyssi = twilio.iloc[:,3]
nejnizsi = twilio.iloc[:,4]
maximum = nejvyssi.max()
minimum = nejnizsi.min()
print(f"Nejnižší hodnota akci byla {minimum}, nejvyšší {maximum}.")