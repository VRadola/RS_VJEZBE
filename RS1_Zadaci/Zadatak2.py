#Napišite program koji traži unos godine i provjerava je li godina prijestupna.

def main():
    #Unos godine
    godina = int(input("Unesite godinu: "))

    #Provejra je li je godina prijestupna
    if(godina % 4 == 0 and (godina % 100 != 0 or godina % 400 == 0)):
        print(f"Godina {godina} je prijestupna godina.")
    else:
        print(f"Godina {godina} nije prijestupna godina.")

if __name__ == "__main__":
    main()