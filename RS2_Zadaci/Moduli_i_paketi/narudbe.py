class Narudba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudbe(self):
        stavke = []
        for proizvod in self.naruceni_proizvodi:
            stavke.append(f"{proizvod['naziv']} x {proizvod['narucena_kolicina']}")

        stavke_string = ", ".join(stavke)
        print(f"Naruceni proizvodi: {stavke_string}, Ukupna cijena: {round(self.ukupna_cijena, 2)} EUR")
        print("-" * 40)

narudbe = []

def napravi_narudbu(lista_proizvoda, skladiste):
    
    if not isinstance(lista_proizvoda, list):
        print("Greska: Argument naruceni_proizvodi mora biti lista.")
        return None
    
    if not lista_proizvoda:
        print("Greska: Lista narucenih proizvoda ne smije biti prazna.")
        return None
    
    potrebni_kljucevi = ['naziv', 'cijena', 'narucena_kolicina']
    
    for i, element in enumerate(lista_proizvoda):
        if not isinstance(element, dict):
            print(f"Greska: Element na indeksu {i} nije rjecnik.")
            return None
        
        if not all(k in element for k in potrebni_kljucevi):
            print(f"Greska: Rjecnik na indeksu {i} nema sve potrebne kljuceve ({', '.join(potrebni_kljucevi)}).")
            return None
            
    for narucena_stavka in lista_proizvoda:
        naziv = narucena_stavka['naziv']
        kolicina = narucena_stavka['narucena_kolicina']
        
        dostupan_proizvod = None
        
        for proizvod_skladiste in skladiste:
            if proizvod_skladiste.naziv == naziv:
                dostupan_proizvod = proizvod_skladiste
                break
        
        if dostupan_proizvod is None:
            print(f"Proizvod {naziv} ne postoji u skladistu i nije dostupan!")
            return None
            
        if dostupan_proizvod.dostupna_kolicina < kolicina:
            print(f"Proizvod {naziv} nije dostupan! Trazeno: {kolicina}, Dostupno: {dostupan_proizvod.dostupna_kolicina}")
            return None
    
    ukupna_cijena = sum(stavka['cijena'] * stavka['narucena_kolicina'] for stavka in lista_proizvoda)
    
    nova_narudzba = Narudba(lista_proizvoda, ukupna_cijena) 
    
    narudbe.append(nova_narudzba)
    print("\n--- NARUDŽBA USPJEŠNO KREIRANA ---")
    
    return nova_narudzba