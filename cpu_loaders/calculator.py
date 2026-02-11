from math import sqrt


def calculator(item_nr: int) -> float:
    print(f"SYNC calculator started for {item_nr} ... ")
    sum = 0
    for item in range(50_000_000):
        sum += sqrt(item)
    print(f"SYNC calculator ended for {item_nr} | sum: {sum}")
    return sum


def heavy_calculator(item_nr: int) -> float:
    print(f"SYNC calculator started for {item_nr} ... ")
    sum = 0
    for item in range(500_000_000):
        sum += sqrt(item)
    print(f"SYNC calculator ended for {item_nr}")
    return sum
