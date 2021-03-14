class Package:
  def __init__(self, address, weightInKilos):
    self.address = address
    self.weightInKilos = weightInKilos
    self.delivered = False

  def getInfo(self):
    return f"Adresa: '{self.address}', hmotnost: {self.weightInKilos}, bylo doruceno: {self.delivered}"

  def deliver(self):
    self.delivered = True
    print(f"Dorucuju balik na {self.address}...")
