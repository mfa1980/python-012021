class Employee:
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Užij si to."
    else:
      return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."

  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."

  def __init__(self, name, position):
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25


class PartTimeEmployee(Employee):
  def getInfo(self):
    return "Je to brigádník."

  def __init__(self, name, position, workload):
    super().__init__(name, position)
    self.workload = workload


brigadnik = PartTimeEmployee("Jirka Pesik", "brigadnik ve skladu", 0.5)
print(brigadnik.getInfo())
