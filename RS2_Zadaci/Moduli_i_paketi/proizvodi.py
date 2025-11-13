class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}")
        print(f"Cijena: {self.cijena} EUR")
        print(f"Dostupna kolicina: {self.dostupna_kolicina}")
        print("-" * 20)
    
skladiste = [
    Proizvod("ASUS ROG STRIX 25", 5000, 5),
    Proizvod("NVIDIA RTX 4080 SUPER", 1000, 10)
]

def dodaj_proizvod(proizvod_dict):
    naziv = f"Proizvod: {proizvod_dict['Naziv']}"
    cijena = f"Cijena: {proizvod_dict['Cijena']}"
    kolicina = f"Dostupna kolicina: {proizvod_dict['Dostupna kolicina']}"

    novi_proizvod = Proizvod(naziv, cijena, kolicina)
    skladiste.append(novi_proizvod)