"""Anti-pattern demo: calling a blocking sync function inside a coroutine.

`synced_sample` is declared `async`, but `synced_wait` blocks the whole
event loop thread — the coroutines run effectively sequentially and the
loop cannot schedule anything else while it sleeps.

Compare with synced_thread_no_block.py which offloads the blocking call
to a worker thread via asyncio.to_thread.
"""

import asyncio
import datetime

from sync_to_async.waiter import synced_wait


async def synced_sample(item):
    """Coroutine that blocks the event loop: `synced_wait` is sync code.

    :param item: identifier printed in the log messages
    """
    print(f'I am item {item}')
    # Blocking call on the event loop thread - nothing else can run meanwhile.
    synced_wait(item=item)


async def run_synced():
    # 10 tasks are scheduled, but each blocks the loop -> ~100s total.
    tasks = [asyncio.create_task(synced_sample(item)) for item in range(10)]
    await asyncio.gather(*tasks)


# Expected output: tasks run one after another, total time ~100s.
if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(run_synced())

    end = datetime.datetime.now()

    print("=" * 20)
    print(f"Total time: {end - start}")
