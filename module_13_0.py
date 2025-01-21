import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(10-power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Serdemian', 3))
    task_2 = asyncio.create_task(start_strongman('Vadim', 4))
    task_3 = asyncio.create_task(start_strongman('Artur', 5))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())

