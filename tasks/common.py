"""Shared helpers for the tasks samples.

Used as a `task.add_done_callback` target so completed tasks are removed
from the tracking set (prevents leaks / premature GC of tasks).
"""

import asyncio


def update_set_state(task: asyncio.Task, background_tasks: set):
    """Done callback: discard the finished task and log the set size.

    :param task: the completed asyncio task
    :param background_tasks: set tracking the still-running tasks
    """
    background_tasks.discard(task)
    print(f"current set is: {len(background_tasks)}")
