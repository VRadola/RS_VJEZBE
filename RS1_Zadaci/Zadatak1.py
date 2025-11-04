"""
Napišite program koji traži od korisnika unos dva broja ( float ) te operator ( + , - , * , / ). Program treba
ispisati rezultat operacije nad unesenim brojevima u formatu:
"""

def main():
    print("Zadatak je pokrenut.")
    # Unos prvog broja
    broj1 = float(input("Unesite prvi broj: "))
    
    # Unos drugog broja
    broj2 = float(input("Unesite drugi broj: "))
    
    # Unos operatora
    operator = input("Unesite operator (+, -, *, /): ")
    
    # Izračunavanje rezultata na osnovu unesenog operatora
    if operator == '+':
        rezultat = broj1 + broj2
    elif operator == '-':
        rezultat = broj1 - broj2
    elif operator == '*':
        rezultat = broj1 * broj2
    elif operator == '/':
        if broj2 != 0:
            rezultat = broj1 / broj2
        else:
            print("Greška: Dijeljenje s nulom nije dozvoljeno.")
            return
    else:
        print("Greška: Nevažeći operator.")
        return
    
    # Ispis rezultata u traženom formatu
    print(f"{broj1} {operator} {broj2} = {rezultat}")

if __name__ == "__main__":
    main()