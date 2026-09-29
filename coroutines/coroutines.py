"""Library of demo coroutines used by the gatherer/tasks samples.

- async_calculator: wraps CPU-bound sync work in a coroutine
  (still blocks the event loop - async does not speed up CPU work).
- my_routine / my_subroutine: I/O-bound style coroutines that sleep.
- *_no_wait variants: same but without awaits - finish instantly.
"""

import asyncio
import random

from cpu_loaders.calculator import calculator


async def async_calculator(routine_nr: int) -> None:
    """Wrap the blocking `calculator` in a coroutine.

    Note: the event loop is blocked while `calculator` runs - this is
    the 'sync work inside async' anti-pattern.

    :param routine_nr: identifier used for logging and the calculation
    """
    print(f"ASYNC calculator started for: {routine_nr} ...")
    sum = calculator(item_nr=routine_nr)
    print(f"ASYNC calculator ended for: {routine_nr} | sum: {sum}")


async def my_subroutine(routine_nr: int) -> None:
    """Sleep 1-5s simulating async I/O (e.g. network call).

    :param routine_nr: identifier used for logging
    """
    print(f"subroutine: {routine_nr} started ...")
    sleeping_time = random.randint(1, 5)
    # Yields control to the event loop while 'sleeping'.
    await asyncio.sleep(sleeping_time)
    print(f"subroutine: {routine_nr} | slept {sleeping_time}")
    print(f"subroutine {routine_nr} ended")


async def my_subroutine_no_wait(routine_nr: int) -> None:
    """Instant subroutine: no awaits, completes immediately.

    :param routine_nr: identifier used for logging
    """
    print(f"subroutine: {routine_nr} started ...")
    print(f"subroutine {routine_nr} ended")


async def my_routine(routine_nr: int) -> None:
    """Sleep, then call a sleeping subroutine - nested async I/O demo.

    :param routine_nr: identifier used for logging
    """
    print(f"routine: {routine_nr} started ...")
    sleeping_time = random.randint(1, 5)
    await asyncio.sleep(sleeping_time)
    await my_subroutine(routine_nr)
    print(f"routine: {routine_nr} | slept {sleeping_time}")
    print(f"routine {routine_nr} ended")


async def my_routine_no_wait(routine_nr: int) -> None:
    """No-sleep variant of my_routine - runs to completion instantly.

    :param routine_nr: identifier used for logging
    """
    print(f"routine: {routine_nr} started ...")
    await my_subroutine(routine_nr)
    print(f"routine {routine_nr} ended")
