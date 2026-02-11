import asyncio
import datetime

from coroutines.coroutines import async_calculator


async def gatherer():
    print("gatherer in")
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
