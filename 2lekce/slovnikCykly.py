sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
"""print("Vydané knížky: ")
for key in sales:
    print(key)"""

  total = 0
  for key, value in sales.items():
    print(f"Knihy {key} se prodalo {value} kusů.")
    total += value
    # total = total + value
  print(f"Celkem bylo prodáno {total} knih.")
  print("Celkem bylo prodáno " + str(total) + " knih.")
