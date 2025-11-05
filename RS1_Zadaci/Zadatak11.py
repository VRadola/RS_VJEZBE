def obrnuti_rijecnik(rijecnik):
    obrnuti = {vrijednost: kljuc for kljuc, vrijednost in rijecnik.items()}
    return obrnuti

def main():
    rijecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
    print(obrnuti_rijecnik(rijecnik))

if __name__ == "__main__":
    main()
    