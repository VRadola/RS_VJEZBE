from proizvodi import *
from narudbe import *

proizvodi_za_dodavanje = [
{"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
{"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
{"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
{"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for proizvod in proizvodi_za_dodavanje:
    proizvod_za_dodati = Proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["dostupna_kolicina"])
    skladiste.append(proizvod_za_dodati)

for proizvod in skladiste:
    proizvod.ispis()

naruceni_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "NVIDIA RTX 4080 SUPER", "cijena": 1000, "narucena_kolicina": 3}
]

napravi_narudbu(naruceni_proizvodi, skladiste)