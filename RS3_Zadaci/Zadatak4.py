import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        return f"Broj {broj} je paran"
    else:
        return f"Broj {broj} je neparan"

async def main():
    random_brojevi = [random.randint(1, 101) for _ in range(10)]
    taskovi = [asyncio.create_task(provjeri_parnost(broj)) for broj in random_brojevi]
    rezultati = await asyncio.gather(*taskovi)
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())