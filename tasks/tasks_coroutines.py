import asyncio
import datetime

from coroutines.coroutines import my_routine
from tasks.common import update_set_state

"""
I/O-bound coroutines as tasks: create_task schedules them, and
await asyncio.wait(...) inside the loop makes each iteration wait for the
previous tasks - useful contrast with tasks_coroutines_no_wait.py.

Tasks WILL NOT stop code from running - scheduling is non-blocking;
the explicit `await asyncio.wait` is what serializes iterations here.
"""


async def tasker_with_coroutines():
    """Schedule sleeping routines as tasks; wait for all in each iteration."""
    background_tasks = set()
    print("tasker_with_coroutines in")

    for item in range(10):
        print(f"task item {item}")
        task = asyncio.create_task(my_routine(item))
        background_tasks.add(task)
        print(f"set is: {len(background_tasks)}")
        task.add_done_callback(lambda t: update_set_state(t, background_tasks))

        # Wait for all pending tasks each iteration; without this the
        # program could exit while tasks are still sleeping.
        if background_tasks:
            await asyncio.wait(background_tasks)

    print("-" * 20)
    print("tasker_with_coroutines out")


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(tasker_with_coroutines())

    end = datetime.datetime.now()

    print("=" * 20)
    print(f"Total time: {end - start}")
