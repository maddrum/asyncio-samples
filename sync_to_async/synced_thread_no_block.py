"""Correct pattern: offload a blocking sync call to a worker thread.

`asyncio.to_thread` runs the SYNC function `synced_wait` in a thread pool,
so the event loop stays free and all 10 items run concurrently.

IMPORTANT: `to_thread` must receive a synchronous callable. Passing a
coroutine function (e.g. `synced_sample`) just creates a coroutine object
that is discarded -> "coroutine was never awaited" warning.

Compare with synced_thread_block.py where the same work runs sequentially.
"""

import asyncio
import datetime

from sync_to_async.waiter import synced_wait


async def synced_sample_to_thread(item):
    """Run the blocking `synced_wait` in a worker thread, freeing the loop.

    :param item: identifier printed in the log messages
    """
    print(f'I am item {item}')
    # Sync callable executed in a separate thread; awaited without blocking.
    await asyncio.to_thread(synced_wait, item)


async def run_synced_to_thread():
    # All 10 threads run in parallel -> total time ~10s instead of ~100s.
    tasks = [asyncio.create_task(synced_sample_to_thread(item)) for item in range(10)]
    await asyncio.gather(*tasks)


# Expected output: tasks run concurrently in threads, total time ~10s.
if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(run_synced_to_thread())

    end = datetime.datetime.now()

    print("=" * 20)
    print(f"Total time: {end - start}")
