import time
import asyncio
import aiohttp
import requests
# 3.1

"""def zadatak(sekunde: int) -> str:
    time.sleep(sekunde)
    print(f"Zadatak zavesen nakon {sekunde} sekundi")


def main():
    print("Izvrsavam main")
    zadatak(3)
    zadatak(2)
    zadatak(1)

t1 = time.perf_counter()
main()
t2 = time.perf_counter()
print(f"Ukupno vrijeme trajanja zadatka je {round(t2 - t1, 2)} sekundi")"""

# 3.2 A
"""async def zadatak(sekunde: int) -> str:
    await asyncio.sleep(sekunde)
    print(f"Zadatak zavesen nakon {sekunde} sekundi")


async def main():
    print("Izvrsavam main")
    task1 = asyncio.create_task(zadatak(3))
    task2 = asyncio.create_task(zadatak(2))
    task3 = asyncio.create_task(zadatak(1))
    rez1 = await task1
    rez2 = await task2
    rez3 = await task3

    return rez1, rez2, rez3


t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Ukupno vrijeme trajanja zadatka je {round(t2 - t1, 2)} sekundi")"""

# 3.2 B
"""async def zadatak(sekunde: int) -> str:
    await asyncio.sleep(sekunde)  #ovjde govore event loopu da ih pozove za x sekundi
    print(f"Zadatak zavesen nakon {sekunde} sekundi")


async def main():
    print("Izvrsavam main") #Event loop izvršava sve dok ne naiđe na await ili dok se ne kreiraju taskovi
    taskovi = [ #kreiramo taskove
    asyncio.create_task(zadatak(3)), #registrira zadatak u event loop i odmah vraćamo kontrolu
    asyncio.create_task(zadatak(2)),
    asyncio.create_task(zadatak(1))
    ]
    
    await asyncio.gather(*taskovi) #pokreće se gather te on govori event loopu da čeka dok svi taskovi ne zavrse

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Ukupno vrijeme trajanja zadatka je {round(t2 - t1, 2)} sekundi")"""

# 3.3
def posalji_zahtjev(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    rezultati = []
    
    for upit in range(3):
        data = posalji_zahtjev(url)
        rezultati.append(data["title"])
    
    print("Dobiveni rezultati", rezultati)

t1 = time.perf_counter()
main()
t2 = time.perf_counter()
print(f"Vrijeme izvrsavanja: {round(t2 - t1, 2)}")

# 3.4
url = "https://jsonplaceholder.typicode.com/todos/1"

async def asiknrono_posalji_zahtjev(url: str, session: aiohttp.ClientSession) -> dict:
    rez = await session.get(url)
    json_odg = await rez.json()
    return json_odg["title"]

async def main():
    async with aiohttp.ClientSession() as session:
        korutine = [asiknrono_posalji_zahtjev(url, session) for _ in range(3)]
        podaci = await asyncio.gather(*korutine)

    print("Podaci: ", podaci)

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrijeme izvrsavanja: {round(t2 - t1, 2)}") #ovaj način je brzi jer radimo asinkrono pomocu event loopa dok u zadatku 3.3 je vrijeme sporije jer response salje blokirajuci zahtjev