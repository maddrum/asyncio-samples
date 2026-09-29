"""Tasks + CPU-bound work: shows tasks alone do NOT parallelize CPU work.

`async_calculator` wraps a blocking sync loop in a coroutine, so even
though tasks are created, each one monopolizes the event loop - work is
effectively sequential. True CPU parallelism needs processes (see
process_pool/).
"""

import asyncio
import datetime

from coroutines.coroutines import async_calculator
from tasks.common import update_set_state


async def tasker():
    """Create 10 calculator tasks, track them in a set, await all."""
    background_tasks = set()
    print("tasker in")

    for item in range(10):
        print(f"task item {item}")
        task = asyncio.create_task(async_calculator(item))
        # Keep a strong reference so the task is not garbage-collected.
        background_tasks.add(task)
        print(f"set is: {len(background_tasks)}")
        task.add_done_callback(lambda t: update_set_state(t, background_tasks))

    if background_tasks:
        # Wait for all remaining tasks before printing 'tasker out'.
        await asyncio.wait(background_tasks)

    print("-" * 20)
    print("tasker out")


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(tasker())

    end = datetime.datetime.now()

    print("=" * 20)
    print(f"Total time: {end - start}")
