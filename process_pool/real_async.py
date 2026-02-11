import asyncio
import datetime
from concurrent.futures import ProcessPoolExecutor

from cpu_loaders.calculator import calculator


async def dispatcher():
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor(max_workers=10) as executor:
        tasks = []
        for item in range(10):
            print(f'Scheduling item {item}')
            # loop.run_in_executor праща задачата към някой от процесите в пула
            # Първият аргумент е executor-ът, следват функцията и нейните аргументи
            task = loop.run_in_executor(executor, calculator, item)
            tasks.append(task)

        # Тук вече изчакваме всички задачи да приключат паралелно
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(dispatcher())

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
