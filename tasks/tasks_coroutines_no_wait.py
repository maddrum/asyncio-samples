import asyncio
import datetime

from coroutines.coroutines import my_routine_no_wait
from tasks.common import update_set_state

"""
Task scheduling without awaits: tasks that never sleep finish instantly.

`my_routine_no_wait` contains no `await asyncio.sleep`, so each task
completes as soon as it gets a loop slot - no need to await them
explicitly. Contrast with tasks_coroutines.py where sleeping tasks
must be awaited or they get cancelled on shutdown.

Tasks WILL NOT stop code from running.
"""


async def tasker_with_coroutines():
    """Schedule 10 instant coroutines as tasks; no explicit wait needed."""
    background_tasks = set()
    print("tasker_with_coroutines in")

    for item in range(10):
        print(f"task item {item}")
        task = asyncio.create_task(my_routine_no_wait(item))
        background_tasks.add(task)
        print(f"set is: {len(background_tasks)}")
        task.add_done_callback(lambda t: update_set_state(t, background_tasks))

        # No need to wait here - the no_wait routines never sleep, so
        # they complete on their own without an explicit await.
        # if background_tasks:
        #     await asyncio.wait(background_tasks)

    print("-" * 20)
    print("tasker_with_coroutines out")
    print("-" * 20)


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(tasker_with_coroutines())

    end = datetime.datetime.now()

    print("=" * 20)
    print(f"Total time: {end - start}")
