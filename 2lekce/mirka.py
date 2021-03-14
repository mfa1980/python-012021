books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

sales = 0
for item in books:
  sales += item["sold"] * item["price"]
print(f"Celkové tržby jsou {sales} Kč.")