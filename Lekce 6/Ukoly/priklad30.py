"""
Export do Excelu
pandas umí uložit data i do Excel sešitu, se kterým se bude uživatelům lépe pracovat.
K ukádání do Excelu využívá pandas modul openpyxl, který ale není nainstalován automaticky.
Nainstaluj si modul openpyxl standardním způsobem, který jsme si ukazovali v lekci.
Ulož tabulku s cekovými počty vykázaných hodin, kterou jsi vytvořila v příkladu 27 jako Excel soubor.
Pokud jsi tento příklad nezpracovala, ulož libovolnou jinou tabulku jako Excel sešit.
Výsledný sešit si otevři a zkontroluj. K uložení použij funkci to_excel, se kterou pracuj stejně,
jako jsme na lekci pracovali s funkci to_csv.
Zkus data z Excelu naopak načíst pomocí funkci read_excel() a ověř, že se soubor načetl v pořádku.
"""
import pandas
import openpyxl
zam_vykazy = pandas.read_csv("zam_vykazy.csv")
print(zam_vykazy.shape)
print(zam_vykazy.head())
zam_vykazy.to_excel("zam_vykazy.xlsx", index=False)
zam_vykazy_nove = pandas.read_excel("zam_vykazy.xlsx")
print(zam_vykazy_nove)
