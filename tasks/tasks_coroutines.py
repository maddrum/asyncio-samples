import asyncio
import datetime

from coroutines.coroutines import my_routine
from tasks.common import update_set_state

"""
Tasks WILL NOT stop code from running
"""


async def tasker_with_coroutines():
    background_tasks = set()
    print("tasker_with_coroutines in")

    for item in range(10):
        print(f"task item {item}")
        task = asyncio.create_task(my_routine(item))
        background_tasks.add(task)
        print(f"set is: {len(background_tasks)}")
        task.add_done_callback(lambda t: update_set_state(t, background_tasks))

        # need to wait all subroutines to be ready otherwise will kill them in their sleep
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
