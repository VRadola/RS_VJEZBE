import asyncio

brojevi = [broj for broj in range(1, 11)]

async def dohvati_listu(lista_brojeva):
    print("Dohvacanje podataka!")
    await asyncio.sleep(3)
    print("Podaci dohvaćeni!")
    return lista_brojeva

async def main():
    print("Korutina pozvana!")
    rezultat = await dohvati_listu(brojevi)
    print(rezultat)

asyncio.run(main())