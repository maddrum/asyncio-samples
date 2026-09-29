"""Baseline: fully synchronous CPU-bound workload.

Runs `calculator` (a heavy sqrt loop) 10 times sequentially - the
slowest variant; used as a reference for the async/process-pool demos.
"""

import datetime

from cpu_loaders.calculator import calculator

# Each calculator call runs to completion before the next starts.
if __name__ == "__main__":
    start = datetime.datetime.now()

    for item in range(10):
        print(f"item {item}")
        calculator(item)

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
