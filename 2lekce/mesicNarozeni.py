"""Měsíc narození
Napiš funkce monthOfBirth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu  vrátí 5."""

def month_of_birt(n):
  #month=n[2:4]
  month = n[2] + n[3]
  month = int(month)
  month = month %50
  return month
print(month_of_birt('9555125899'))
