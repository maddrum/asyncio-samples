import asyncio
import datetime

from coroutines.coroutines import my_routine

"""
Gatherer WILL stop code from running.
`gatherer out` will appear only after all tasks are completed.
"""


async def gatherer():
    print("gatherer in")
    tasks = [my_routine(item) for item in range(10)]
    await asyncio.gather(*tasks)
    print("-" * 20)
    print("gatherer out")


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(gatherer())

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
