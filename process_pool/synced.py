"""Anti-pattern: a ProcessPoolExecutor that is never actually used.

The executor is created but `calculator` is called directly in the loop,
so everything runs sequentially on the event loop thread. Kept as a
contrast to real_async.py which submits work via run_in_executor.
"""

import asyncio
import datetime
from concurrent.futures import ProcessPoolExecutor

from cpu_loaders.calculator import calculator


async def dispatcher():
    """Create a pool but call calculator inline - effectively sequential."""
    # problem is that it only execute one at a time
    # this is synced
    with ProcessPoolExecutor(max_workers=10) as executor:
        for item in range(10):
            print(f"item {item}")
            # BUG-by-demo: direct call ignores the pool entirely -
            # blocks the event loop, one item at a time.
            calculator(item_nr=item)


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(dispatcher())

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
