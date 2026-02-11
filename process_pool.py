import asyncio
import datetime

from cpu_loaders.calculator import calculator


async def dispatcher():
    for item in range(10):
        print(f"item {item}")
        calculator(item)


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(dispatcher())

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
