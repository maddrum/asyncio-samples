"""asyncio.gather over CPU-bound coroutines.

Gathers 10 `async_calculator` coroutines, but since each wraps blocking
sync work, they still run sequentially on the event loop. Contrast with
gatherer_routine.py where sleeping coroutines actually overlap.
"""

import asyncio
import datetime

from coroutines.coroutines import async_calculator


async def gatherer():
    """Run 10 calculator coroutines concurrently via asyncio.gather.

    'gatherer out' prints only after ALL coroutines finish - gather
    blocks until every task completes.
    """
    print("gatherer in")
    # Bare coroutines: gather schedules them as tasks implicitly.
    tasks = [async_calculator(item) for item in range(10)]
    await asyncio.gather(*tasks)
    print("-" * 20)
    print("gatherer out")


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(gatherer())

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
