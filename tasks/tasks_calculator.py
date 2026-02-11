import asyncio
import datetime

from coroutines.coroutines import async_calculator
from tasks.common import update_set_state


async def tasker():
    background_tasks = set()
    print("tasker in")

    for item in range(10):
        print(f"task item {item}")
        task = asyncio.create_task(async_calculator(item))
        background_tasks.add(task)
        print(f"set is: {len(background_tasks)}")
        task.add_done_callback(lambda t: update_set_state(t, background_tasks))

    if background_tasks:
        await asyncio.wait(background_tasks)

    print("-" * 20)
    print("tasker out")


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(tasker())

    end = datetime.datetime.now()

    print("=" * 20)
    print(f"Total time: {end - start}")
