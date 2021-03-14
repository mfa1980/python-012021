"""Vysvědčení
Uvažujme vysvědčení, které máme zapsané jako slovník.

Napiš program, který spočte průměrnou známku ze všech předmětů.
Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1."""

schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělešná výchova": 3,
  "Chemie": 4,
}

sum_marks = 0
for subject, mark in schoolReport.items():
  sum_marks+=mark

  if mark==1:
    subject.append
print(sum(schoolReport.values()/len(schoolReport)))