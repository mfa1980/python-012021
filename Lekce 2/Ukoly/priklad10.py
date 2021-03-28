"""
Klíč k úspěchu
Obchodníci v naší softwarové firmě používají jednoduchý systém, aby odhadli šanci
na úspěch potenciální zakázky. Každé zakázce přiřadí body od 0 do 10 a platí:

Pokud má zakázka méně než 5 bodů, šance na záskání je malá.
Pokud má zakázka 6 až 8 bodů, šance na získání je střední.
Pokud má zakázka více bodů, šance na získání je vysoká.
Body přidělují podle následujících kritérií:

Odvětví: Firma nejlépe prodává do automotive, o něco hůře do retailu. Pokud potenciální zákazník
podniká v automotive, přičti 3 body, pokud v retailu, přičti 2 bod, jinak 0.
Obrat: Firma nejlépe prodává zákazníkům se středním obratem. U malých většinou neuspěje,
u velkých občas ano. Pokud má firma obrat menší než 10 mil. Euro, přičti 0.
Pokud je mezi 10 a 1 000 mil. Euro, přičti 3 body, jinak 1 bod.
Země: Firma je nejúspěšnější v Česku a na Slovensku (2 body), o něco méně v Německu a ve Francii (1 bod).
Ostatním zemím dej 0.
Konference: Firma loni pořádala odbornou konferenci pro zákazníky.
Pokud se zákazník konference účastnil, přičti 1 bod, jinak 0.
Newsletter: Firma též rozesílá newsletter o svém produktu. Pokud zákazník newsletter odebírá, přičti 1 bod.
Napiš funkci, které bude mít 5 parametrů, které reprezentují zadaná kritéria.
Poslední dvě kritéria zadej jako nepovinná s výchozí hodnotou False.
Funkce vrátí šanci na získání zakázky jako řetězec.
"""

def funkce_body(kriterium_1,kriterium_2,kriterium_3,kriterium_4=0,kriterium_5=0):
  soucet = 0
  if kriterium_1 == "A":
    soucet += 3
  elif kriterium_1 == "B":
    soucet += 2
  if kriterium_2 == "B":
    soucet += 3
  elif kriterium_2 == "C":
    soucet += 1
  if kriterium_3 == "A":
    soucet += 3
  elif kriterium_3 == "B":
    soucet += 1
  if kriterium_4 == "A":
    soucet += 1
  if kriterium_5 == "A":
    soucet += 1
  if soucet <= 5:
    print("Šance na záskání je malá.")
  elif soucet >=6 and soucet <=8:
    print("Šance na získání je střední")
  elif soucet > 8:
    print("Šance na získání je vysoká")
  print(soucet)

kriterium_1 = input("Vyber oblast podnikání: A - automotive, B - retail, C - ostatní: ")
kriterium_2 = input("Jaký máš obrat?: A - do 10 mil. EUR, B - 10-100 mil. EUR, C - nad 100 mil EUR: ")
kriterium_3 = input("Z jaké jsi země? A - Česká republika či Slovensko, B - Německo, Francie, C - ostatní: ")
kriterium_4 = input("Byl jsi na naší konferenci? A - ano, B - ne: ")
kriterium_5 = input("Odebíráš náš newsletter? A - ano, B - ne: ")

funkce_body(kriterium_1,kriterium_2,kriterium_3,kriterium_4=0,kriterium_5=0)