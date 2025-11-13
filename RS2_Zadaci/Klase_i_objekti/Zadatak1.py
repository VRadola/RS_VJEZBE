from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza
    
    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraza: {self.kilometraza}")

    def starost(self):
        trenutna_godina = datetime.now().year
        starost_automobila = trenutna_godina - self.godina_proizvodnje
        print(f"Starost automobila je: {starost_automobila}")

auto1 = Automobil("BMW", "Serija 3", 2009, 250000)
auto1.ispis()
auto1.starost()
print(30*"-")
auto2 = Automobil("Audi", "A6", 2003, 350000)
auto2.ispis()
auto2.starost()