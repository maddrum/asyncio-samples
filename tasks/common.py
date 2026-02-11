import asyncio


def update_set_state(task: asyncio.Task, background_tasks: set):
    background_tasks.discard(task)
    print(f"current set is: {len(background_tasks)}")
