import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1): #za zadani range radimo blok koda
        print(f'{name}: {i} sekundi preostalo...') #ispis imena timera i koliko je preostalo sekundi
        await asyncio.sleep(1) #simulacija da dohvaćanje traje 1 sekundu
    print(f'{name}: Vrijeme je isteklo!') #Za svaki timer kada odbroji ispisujemo da je isteklo vrijeme

async def main():
    timers = [ 
    asyncio.create_task(timer('Timer 1', 3)), #schedule
    asyncio.create_task(timer('Timer 2', 5)), #schedule
    asyncio.create_task(timer('Timer 3', 7)) #schedule
    ]
    await asyncio.gather(*timers) #pokretanje svih timera istovremeno

asyncio.run(main())