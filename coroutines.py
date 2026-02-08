import asyncio
import random
from math import sqrt


async def subroutine(routine_nr: int) -> None:
    print(f"subroutine: {routine_nr}")
    sleeping_time = random.randint(1, 5)
    await asyncio.sleep(sleeping_time)
    await calc_something(routine_nr)
    print(f"subroutine: {routine_nr} | slept {sleeping_time}")
    print(f"subroutine {routine_nr} ended")


async def calc_something(routine_nr: int) -> None:
    print(f"calc_something: {routine_nr}")
    sum = 0
    for item in range(random.randint(10_000_000, 100_000_000)):
        sum += sqrt(item)
    print(f"calc_something: {routine_nr} | sum: {sum}")
    print(f"calc_something {routine_nr} ended")


async def routine(routine_nr: int) -> None:
    print(f"routine: {routine_nr}")
    sleeping_time = random.randint(1, 5)
    await asyncio.sleep(sleeping_time)
    await subroutine(routine_nr)
    print(f"routine: {routine_nr} | slept {sleeping_time}")
    print(f"routine {routine_nr} ended")
