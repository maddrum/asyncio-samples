"""Minimal demo: a single create_task + await.

Shows that create_task returns immediately (the task is scheduled, not
run to completion), and that you must `await` the task or it may be
cancelled when the event loop shuts down.
"""

import asyncio
import datetime

from coroutines.coroutines import my_routine


async def tasker_with_single_coroutine():
    """Schedule one sleeping routine as a task and await its completion."""
    print("tasker_with_single_coroutine in")

    item = 5
    print(f"task item {item}")
    task = asyncio.create_task(my_routine(item))

    # done immediately
    print("task is added")

    # need to await it otherwise will not complete - gets killed in their sleep
    await task

    # done after routine and coroutine
    print("-" * 20)
    print("tasker_with_coroutines out")


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(tasker_with_single_coroutine())

    end = datetime.datetime.now()

    print("=" * 20)
    print(f"Total time: {end - start}")
