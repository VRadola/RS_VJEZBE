"""
Implementirajte igru pogađanja broja u rasponu od 1 do 100. Svaki pokušaj pogađanja sastoji se od unosa
pretpostavljenog broja te ispisa odgovora je li uneseni broj veći, manji ili jednak broju koji treba pogoditi.
Igra se nastavlja sve dok korisnik ne pogodi broj.
"""

import random

def pogodi_broj():
    izabrani_broj = random.randint(1, 100) #Racunalo odabire broj
    broj_je_pogoden = False #Inicijalizacija varijable na False da igra moze poceti
    broj_pokusaja = 0 #Brojac pokusaja igraca
    #Igra pocinje
    print("Igra: Pododi broj izmedu 1 i 100!")
    player_number = int(input("Tvoj broj: ")) #Unos prvog pokusaja igraca17
    while not broj_je_pogoden:
        if player_number < izabrani_broj:
            broj_pokusaja += 1
            print("Uneseni broj je manji od trazenog broja.")
            player_number = int(input("Pokusaj ponovo: "))
        elif player_number > izabrani_broj:
            broj_pokusaja += 1
            print("Uneseni broj je veci od trazenog broja.")
            player_number = int(input("Pokusaj ponovo: "))
        else:
            broj_je_pogoden = True
            print("Cestitamo! Pogodili ste broj.\nBroj pokusaja: ", broj_pokusaja)

def main():
    pogodi_broj()

if __name__ == "__main__":
    main()