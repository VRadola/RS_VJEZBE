




def validiraj_broj_telefona(broj: str):
    # FIKSNE MREŽE
    fiksne_mreže = {
        "01": "Grad Zagreb i Zagrebačka županija",
        "020": "Dubrovačko-neretvanska županija",
        "021": "Splitsko-dalmatinska županija",
        "022": "Šibensko-kninska županija",
        "023": "Zadarska županija",
        "031": "Osječko-baranjska županija",
        "032": "Vukovarsko-srijemska županija",
        "033": "Virovitičko-podravska županija",
        "034": "Požeško-slavonska županija",
        "035": "Brodsko-posavska županija",
        "040": "Međimurska županija",
        "042": "Varaždinska županija",
        "043": "Bjelovarsko-bilogorska županija",
        "044": "Sisačko-moslavačka županija",
        "047": "Karlovačka županija",
        "048": "Koprivničko-križevačka županija",
        "049": "Krapinsko-zagorska županija",
        "051": "Primorsko-goranska županija",
        "052": "Istarska županija",
        "053": "Ličko-senjska županija"
    }
    
    # MOBILNE MREŽE
    mobilne_mreže = {
        "091": "A1 Hrvatska",
        "092": "Tomato",
        "095": "Telemach",
        "097": "bonbon",
        "098": "Hrvatski Telekom",
        "099": "Hrvatski Telekom"
    }
    
    # POSEBNE USLUGE
    posebne_usluge = {
        "0800": "Besplatni pozivi",
        "060": "Komercijalni pozivi",
        "061": "Glasovanje telefonom",
        "064": "Usluge s neprimjerenim sadržajem",
        "065": "Nagradne igre",
        "069": "Usluge namijenjene djeci",
        "072": "Jedinstveni pristupni broj za posebne usluge"
    }

    rezultat = {
        "pozivni_broj": None,
        "broj_ostatak": None,
        "vrsta_mreže": None,
        "mjesto": None,
        "operater": None,
        "validan": False
    }

    def ocisti_broj(broj):
        for znak in [" ", "-", "(", ")"]:
            broj = broj.replace(znak, "")
            if broj.startswith("+385"):
                broj = "0" + broj[4:]
            elif broj.startswith("00385"):
                broj = "0" + broj[5:]
        return broj
    
    broj = ocisti_broj(broj)

    svi_pozivni_brojevi = list(fiksne_mreže.keys()) + list(mobilne_mreže.keys()) + list(posebne_usluge.keys())
    svi_pozivni_brojevi.sort(key=len, reverse=True)

    pozivni_broj = None
    for pb in svi_pozivni_brojevi:
        if broj.startswith(pb):
            pozivni_broj = pb
            break
    
    if pozivni_broj is None:
        return rezultat
    
    broj_ostatak = broj[len(pozivni_broj):]

    rezultat["pozivni_broj"] = pozivni_broj
    rezultat["broj_ostatak"] = broj_ostatak

    if pozivni_broj in fiksne_mreže:
        rezultat["vrsta_mreže"] = "fiksna"
        rezultat["mjesto"] = fiksne_mreže[pozivni_broj]
        rezultat["operater"] = None
        if len(broj_ostatak) in [6, 7]:
            rezultat["validan"] = True

    elif pozivni_broj in mobilne_mreže:
        rezultat["vrsta_mreže"] = "mobilna"
        rezultat["mjesto"] = None
        rezultat["operater"] = mobilne_mreže[pozivni_broj]
        if len(broj_ostatak) in [6, 7]:
            rezultat["validan"] = True
        
    elif pozivni_broj in posebne_usluge:
        rezultat["vrsta_mreže"] = "posebna usluga"
        rezultat["mjesto"] = None
        rezultat["operater"] = None
        if len(broj_ostatak) == 6:
            rezultat["validan"] = True
    
    return rezultat

if __name__ == "__main__":
    test_brojevi = [
        "+385 1 1234567",
        "00385-91-6543210",
        "0800 123 456",
        "(049) 7654321",
        "061-234567",
        "0991234567",
        "12345"
    ]
    
    for broj in test_brojevi:
        rezultat = validiraj_broj_telefona(broj)
        print(f"Broj: {broj} -> {rezultat}")
