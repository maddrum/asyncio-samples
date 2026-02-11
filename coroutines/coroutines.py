import asyncio
import random

from cpu_loaders.calculator import calculator


async def async_calculator(routine_nr: int) -> None:
    print(f"ASYNC calculator started for: {routine_nr} ...")
    sum = calculator(item_nr=routine_nr)
    print(f"ASYNC calculator ended for: {routine_nr} | sum: {sum}")


async def my_subroutine(routine_nr: int) -> None:
    print(f"subroutine: {routine_nr} started ...")
    sleeping_time = random.randint(1, 5)
    await asyncio.sleep(sleeping_time)
    print(f"subroutine: {routine_nr} | slept {sleeping_time}")
    print(f"subroutine {routine_nr} ended")


async def my_subroutine_no_wait(routine_nr: int) -> None:
    print(f"subroutine: {routine_nr} started ...")
    print(f"subroutine {routine_nr} ended")


async def my_routine(routine_nr: int) -> None:
    print(f"routine: {routine_nr} started ...")
    sleeping_time = random.randint(1, 5)
    await asyncio.sleep(sleeping_time)
    await my_subroutine(routine_nr)
    print(f"routine: {routine_nr} | slept {sleeping_time}")
    print(f"routine {routine_nr} ended")


async def my_routine_no_wait(routine_nr: int) -> None:
    print(f"routine: {routine_nr} started ...")
    await my_subroutine(routine_nr)
    print(f"routine {routine_nr} ended")
