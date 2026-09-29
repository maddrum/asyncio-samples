"""CPU-bound workloads shared by all samples.

Pure synchronous number crunching used to demonstrate the difference
between sync execution, asyncio tasks (no help for CPU work), and
process pools (real parallelism).
"""

from math import sqrt


def calculator(item_nr: int) -> float:
    """Sum sqrt(i) for 50M iterations - heavy CPU-bound work.

    :param item_nr: identifier used for logging
    :return: the computed sum
    """
    print(f"SYNC calculator started for {item_nr} ... ")
    sum = 0
    for item in range(50_000_000):
        sum += sqrt(item)
    print(f"SYNC calculator ended for {item_nr} | sum: {sum}")
    return sum


def heavy_calculator(item_nr: int) -> float:
    """Same as `calculator` but 10x iterations - even heavier load.

    :param item_nr: identifier used for logging
    :return: the computed sum
    """
    print(f"SYNC calculator started for {item_nr} ... ")
    sum = 0
    for item in range(500_000_000):
        sum += sqrt(item)
    print(f"SYNC calculator ended for {item_nr}")
    return sum
