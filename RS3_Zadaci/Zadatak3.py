import asyncio

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik_iz_baze, unesena_lozinka):
    await asyncio.sleep(2)
    lozinka_baza = None
    for loz in baza_lozinka:
        if loz["korisnicko_ime"] == korisnik_iz_baze["korisnicko_ime"]:
            lozinka_baza = loz["lozinka"]
            break

    if lozinka_baza == unesena_lozinka:
        return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija uspjesna!"
    else:
        return f"Korisnik {korisnik_iz_baze['korisnicko_ime']}: Autorizacija neuspjesna!"

async def autentifikacija(rijecnik):
    await asyncio.sleep(3)
    korisnik_baza = None
    for korisnik in baza_korisnika:
        if (korisnik["korisnicko_ime"] == rijecnik["korisnicko_ime"] and 
            korisnik["email"] == rijecnik["email"]):
            korisnik_baza = korisnik
            break
    if korisnik_baza is None:
        return f"Korisnik {rijecnik} nije pronaden!"
    rezultat = await autorizacija(korisnik_baza, rijecnik["lozinka"])
    return rezultat

async def main():
    test = {"korisnicko_ime": "ana_anic",
            "email": "aanic@gmail.com",
            "lozinka": "super_teska_lozinka"
            }
    
    rezultat = await autentifikacija(test)
    print(rezultat)

asyncio.run(main())