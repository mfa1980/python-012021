item = {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True}
key = "price"
item[key]= 929
print("Vybraný předmět je "  + item["title"] + "a cena je " + str(item["price"]) + ".")
print ("Vybraný předmět je", item["title"], "a cena je", item["price"], ".")
print(f"Vybraný předmět je {item['title']} a cena je {item['price']}.")
item["weight"] = 0.6
if "weight" in item:
  print(f"Hmotnost předmětu je {item['weight']}")
else:
  print("Hmotnost není zadána.")
