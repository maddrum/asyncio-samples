import asyncio
import datetime
from concurrent.futures import ProcessPoolExecutor

from cpu_loaders.calculator import calculator


async def dispatcher():
    # problem is that it only execute one at a time
    # this is synced
    with ProcessPoolExecutor(max_workers=10) as executor:
        for item in range(10):
            print(f"item {item}")
            calculator(item_nr=item)


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(dispatcher())

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
