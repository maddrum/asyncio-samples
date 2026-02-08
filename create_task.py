import asyncio
import datetime

from coroutines import async_calculator

background_tasks = set()


def print_set_state(task: asyncio.Task):
    print(f"set is: {len(background_tasks)}")
    background_tasks.discard(task)


async def tasker():
    print("tasker in")

    for item in range(10):
        print(f"task item {item}")
        task = asyncio.create_task(async_calculator(item))
        background_tasks.add(task)
        print(f"set is: {len(background_tasks)}")
        task.add_done_callback(print_set_state)

    print("-" * 20)
    print("tasker out")


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(tasker())

    end = datetime.datetime.now()
    print("Final set is:", len(background_tasks))
    print("=" * 20)
    print(f"Total time: {end - start}")
