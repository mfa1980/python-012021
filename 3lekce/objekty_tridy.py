class Employee:
  def take_holiday(self, days):
    if self.holidays >= days:
      self.holidays -= days
      return "Dovolená schválena."
    else:
      return f"Můžeš si vzít pouze {self.holidays} dnů."

  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}"

  def __str__(self):
    return self.name

  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.holidays = 25


frantisek = Employee("František Novák", "konstruktér")
klara = Employee("Klára Nová", "konstruktérka")
print(frantisek.take_holiday(10))
print(frantisek.take_holiday(10))
print(frantisek.take_holiday(10))
