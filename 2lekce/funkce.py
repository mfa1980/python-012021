"""def greetUser(name):
  print(f"Ahoj {name}")
greetUser("Mirko")
def sumTwoNumbers(a, b):
  return a+b
result = sumTwoNumbers(5, 9)
print(result)

Pár příkladů využití funkcí
Vraťme se k našemu příkladu z opakovací lekce, kde jsme měli určit známku z testu na základě počtu bodů.
Uvažujme nyní, že student, který získá z testu známku 5, má možnost test jedenkrát opakovat.
Podmínku, kterou jsme měli v prvním cvičení, tedy budeme potřebovat dvakrát - pro první a případný
druhý pokus. Proto je ideální tuto podmínku umístit do funkce."""

def getMark(points, bonus=0):
  if points + bonus <= 60:
    mark = 5
  elif points + bonus<= 70:
    mark = 4
  elif points + bonus<= 80:
    mark = 3
  elif points + bonus<= 90:
    mark = 2
  else:
    mark = 1
  return mark
points = input("Zadej počet bodů: ")
points = int(points)
bonus = input("Zadej počet bonusových bodů: ")
bonus = int(bonus)
mark = getMark(points, bonus)
if mark ==5:
  points =  input("Počet bodů u opravného testu: ")
  points = int(points)
  mark = getMark(points)
print(f"Výsledná zámka je {mark}.")