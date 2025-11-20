import asyncio

rijecnik1 = [{"ime" : "Vito", "prezime" : "Radola", "god_rod" : 2000},
             {"ime" : "Marko", "prezime" : "Markic", "god_rod" : 2002},
             {"ime" : "Ana", "prezime" : "Anic", "god_rod" : 1998}
             ]

rijecnik2 = [{"naziv" : "Laptop", "cijena" : 1500, "stanje_na_skladistu" : 20},
             {"naziv" : "Graficka kartica", "cijena" : 2000, "stanje_na_skladistu" : 12},
             {"naziv" : "Mis", "cijena" : 10, "stanje_na_skladistu" : 50},
             {"naziv" : "Web kamera", "cijena" : 90, "stanje_na_skladistu" : 100},
             {"naziv" : "Tipkovnica", "cijena" : 40, "stanje_na_skladistu" : 15},
             {"naziv" : "Zvucnik", "cijena" : 200, "stanje_na_skladistu" : 8}
             ]

async def korutina1(rijecnik):
    print("Dohvacanje podataka prve korutine!")
    await asyncio.sleep(3)
    print("Podaci korutine 1 su dohvaceni!")
    return rijecnik

async def korutina2(rijecnik):
    print("Dohvaćane podataka druge korutine!")
    await asyncio.sleep(5)
    print("Podaci korutine 2 su dohvaceni!")
    return rijecnik

async def main():
    print("Izvrsavanje main")
    task1 = asyncio.create_task(korutina1(rijecnik1))
    task2 = asyncio.create_task(korutina2(rijecnik2))
    rezultat = await task1
    rezultat2 = await task2
    asyncio.gather(task1, task2)
    print("\n--- Rijecnik 1 ---")
    for osoba in rezultat:
        print(osoba)

    print("\n--- Rijecnik 2 ---")
    for proizvod in rezultat2:
        print(proizvod)

asyncio.run(main())