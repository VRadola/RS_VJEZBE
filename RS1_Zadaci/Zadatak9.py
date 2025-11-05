import string

def brojac_rijeci(tekst):
    ponavljanje_rijeci = {}

    normalni_tekst = tekst.lower()

    for znak in string.punctuation:
        normalni_tekst = normalni_tekst.replace(znak, "")
    
    rijeci = normalni_tekst.split()

    for rijec in rijeci:
        if not rijec:
            continue

        ponavljanje_rijeci[rijec] = ponavljanje_rijeci.get(rijec, 0) + 1
    
    return ponavljanje_rijeci

def main():
    tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je " \
    "vrlo popularan."
     
    rezultat = brojac_rijeci(tekst)
    print(f"Rezultat recenice:'")
    print("-" * 15)
    for rijec, count in rezultat.items():
        print(f"'{rijec}': {count}")

if __name__ == "__main__":
    main()