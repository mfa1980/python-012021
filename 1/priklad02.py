"""
Skladník
Vyvíjíš software pro obchod s elektronickými součástkami.
Firma eviduje informace o počtu součástek na skladě ve slovníku.
Klíč slovníku je kód součástky a číslo je počet součástek na skladě.
Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník.
Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit.
Obě informace si ulož. Následně naprogramuj následující varianty:
Pokud zadaný zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom,
že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši,
a sniž počet součástek na skladě o množství požadované zákazníkem.
"""
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Zadej kód součástky: ")
if kod not in sklad:
  print("Součástka není skladem.")
else:
  pocet = int(input("Zadej počet kusů: "))
  if pocet >= sklad[kod]:
    print("Lze prodat pouze omezené množství.")
    sklad.pop(kod)
  else:
    print("Poptávku lze uspokojit v plné výši.")
    sklad[kod]=sklad[kod] - pocet
print(sklad)