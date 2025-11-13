class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"{self.ime} radi na poziciji {self.pozicija}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department, povecanje):
        super().__init__(ime, pozicija, placa)
        self.department = department
        self.povecanje = povecanje

    def work(self):
        print(f"{self.ime} radi na poziciji {self.pozicija} u odjelu {self.department}")

    def give_raise(self, radnik):
        nova_placa = radnik.placa + self.povecanje
        print(f"{radnik.ime} dobiva povisicu od {self.povecanje}, te mu je nova placa: {nova_placa}")

r = Radnik("Marko", "Inženjer", 8000)
m = Manager("Ana", "Voditelj", 15000, "Razvoj", 1000)

print("--- Mjesto rada ---")
r.work()
m.work()

print("\n--- Povišica ---")
m.give_raise(r)