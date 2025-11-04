def main():
    broj = int(input("Unesite broj za izracunavanje faktoriala: "))
    rezultat = 1
    while broj >1:
        rezultat *= broj
        broj -= 1
    print(f"Faktorial broja je {rezultat}")

if __name__ == "__main__":
    main()