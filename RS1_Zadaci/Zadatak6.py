import string

def provjera_lozinke(lozinka):
    min_duzina_lozinke = 8
    max_duzina_lozinke = 15

    duzina_lozinke = len(lozinka)
    if not (min_duzina_lozinke <= duzina_lozinke <= max_duzina_lozinke):
        return f"Lozinka mora sadrzavati izmedu {min_duzina_lozinke} i {max_duzina_lozinke} znakova"

    ima_veliko_slovo = any(znamenka.isupper() for znamenka in lozinka)
    ima_broj = any(broj.isdigit() for broj in lozinka)
    if not (ima_veliko_slovo and ima_broj):
        return "Lozinka mora sadrzavati barem jedno veliko slovo i broj"
    
    zabranjena_lozinka = lozinka.lower()
    zabranjene_lozinke = ["password", "lozinka"]
    for rijec in zabranjene_lozinke:
        if rijec in zabranjena_lozinka:
            return f"Lozinka nesmije sadrzavati {rijec}"
    
    return None

def validacija():
    while (True):
        lozinka = input("Unesite lozinku za provjeru jakosti: ")
        rezultat_provjere = provjera_lozinke(lozinka)

        if rezultat_provjere is None:
            print("Lozinka je jaka")
        else:
            print(f"Greska: {rezultat_provjere}")

validacija()