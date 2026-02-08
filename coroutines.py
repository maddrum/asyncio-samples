import asyncio
import random
from math import sqrt


def calculator(item_nr: int) -> float:
    print(f"SYNC calculator started for {item_nr} ... ")
    sum = 0
    for item in range(random.randint(10_000_000, 100_000_000)):
        sum += sqrt(item)
    print(f"SYNC calculator ended for {item_nr}")
    return sum


async def async_calculator(routine_nr: int) -> None:
    print(f"ASYNC calculator started for: {routine_nr} ...")
    sum = calculator(item_nr=routine_nr)
    print(f"ASYNC calculator ended for: {routine_nr} | sum: {sum}")


async def subroutine(routine_nr: int) -> None:
    print(f"subroutine: {routine_nr} started ...")
    sleeping_time = random.randint(1, 5)
    await asyncio.sleep(sleeping_time)
    await async_calculator(routine_nr)
    print(f"subroutine: {routine_nr} | slept {sleeping_time}")
    print(f"subroutine {routine_nr} ended")


async def routine(routine_nr: int) -> None:
    print(f"routine: {routine_nr} started ...")
    sleeping_time = random.randint(1, 5)
    await asyncio.sleep(sleeping_time)
    await subroutine(routine_nr)
    print(f"routine: {routine_nr} | slept {sleeping_time}")
    print(f"routine {routine_nr} ended")
