import asyncio
import hashlib

zadaci = [
    {"prezime": "Radola", "broj_kartice": 1234556, "CVV": 123},
    {"prezime": "Car", "broj_kartice": 6654321, "CVV": 321},
    {"prezime": "Baja", "broj_kartice": 1122334, "CVV": 112}
]

async def secure_data(podaci):
    await asyncio.sleep(3)
    enkriptirani_broj = hash(str(podaci["broj_kartice"]))
    enkriptirani_cvv = hash(str(podaci["CVV"]))

    return {
        "prezime": podaci["prezime"],
        "broj_kartice": enkriptirani_broj,
        "CVV": enkriptirani_cvv
    }

async def main():
    taskovi = [asyncio.create_task(secure_data(podatak)) for podatak in zadaci]
    rezultati = await asyncio.gather(*taskovi)

    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())