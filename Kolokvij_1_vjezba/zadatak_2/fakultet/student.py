from fakultet.podaci import razredi_studenti

moguci_razredi = set(element["razred"] for element in razredi_studenti)

class Student:
    def __init__(self, ime: str, prezime: str, razred: str, kolegij_ocjene: dict):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.kolegij_ocjene = kolegij_ocjene

    def prosjek_ocjene(self):
        if not self.kolegij_ocjene:
            return 0.0
        else:
            prosjek = round(sum(ukupno for ukupno in self.kolegij_ocjene.values()) / len(self.kolegij_ocjene), 1)
            return prosjek
        
    def promjena_razreda(self, novi_razred):
        if novi_razred not in moguci_razredi:
            return "Negdje si pogriješio"
        else:
            self.razred = novi_razred