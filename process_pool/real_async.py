"""Asyncio + ProcessPoolExecutor: the correct way to do CPU-bound work
from async code.

`loop.run_in_executor` submits `calculator` to a process pool, so the
event loop stays responsive AND the CPU work runs in parallel across
processes. Compare with synced.py (sequential) and tasks_calculator.py
(blocked event loop).
"""

import asyncio
import datetime
from concurrent.futures import ProcessPoolExecutor

from cpu_loaders.calculator import calculator


async def dispatcher():
    """Submit 10 calculator jobs to a process pool and await all."""
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor(max_workers=10) as executor:
        tasks = []
        for item in range(10):
            print(f'Scheduling item {item}')
            # loop.run_in_executor праща задачата към някой от процесите в пула
            # Първият аргумент е executor-ът, следват функцията и нейните аргументи
            task = loop.run_in_executor(executor, calculator, item)
            tasks.append(task)

        # Await all futures: the loop is free while processes crunch.
        # Тук вече изчакваме всички задачи да приключат паралелно
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(dispatcher())

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
