"""
Projekty
Pokračuj ve své práci pro softwarovou firmu. Ze souboru vykazy.csv načti informace o výkazech na
projekty pro jednoho vybraného zákazníka.
Načti data ze souboru a ulož je do tabulky.
Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.
Dobrovolný doplněk
Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení.
Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře, tj. spočítej celkový počet
hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.
"""
#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")
import pandas
vykazy = pandas.read_csv("vykazy.csv").dropna()
print(vykazy.groupby("project")["hours"].count())

import pandas
praha = pandas.read_csv("zam_praha.csv").dropna()
plzen = pandas.read_csv("zam_plzeň.csv").dropna()
liberec = pandas.read_csv("zam_liberec.csv").dropna()
praha["mesto"] = "Praha"
plzen["mesto"] = "Plzeň"
liberec["mesto"] = "Liberec"
zamestnanci = pandas.concat([praha,plzen,liberec], ignore_index = True)
vykazy = vykazy.rename(columns={"emloyee_id": "cislo_zamestnance"})
zam_vykazy = pandas.merge(zamestnanci,vykazy)
zam_vykazy.to_csv("zam_vykazy.csv", index=False)
print(zam_vykazy.columns)
print(zam_vykazy.groupby(["project","mesto"])["hours"].count())
