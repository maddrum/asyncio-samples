import asyncio
import datetime

from coroutines.coroutines import my_routine

"""asyncio.gather over I/O-bound (sleeping) coroutines.

All 10 routines run concurrently - total time is ~max sleep (~10s for
two sequential 1-5s sleeps per routine), not the sum. Demonstrates real
concurrency for I/O-bound work.

Gatherer WILL stop code from running.
`gatherer out` will appear only after all tasks are completed.
"""


async def gatherer():
    """Run 10 sleeping routines concurrently via asyncio.gather."""
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
