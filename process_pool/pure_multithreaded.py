"""Raw multiprocessing: real CPU parallelism without asyncio.

Spawns 10 OS processes, each running `calculator`. Processes bypass the
GIL, so CPU-bound work runs truly in parallel (up to core count).
Note: despite the filename, these are processes, not threads.
"""

import datetime
import multiprocessing

from cpu_loaders.calculator import calculator

if __name__ == "__main__":
    start = datetime.datetime.now()

    processes = []
    for thread in range(10):
        # Each Process runs calculator() in a separate OS process.
        process = multiprocessing.Process(target=calculator, kwargs={"item_nr": thread})
        process.start()
        processes.append(process)

    # Block until every process finishes.
    for process in processes:
        process.join()

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
