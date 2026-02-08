import datetime

from coroutines import calculator

if __name__ == "__main__":
    start = datetime.datetime.now()

    for item in range(10):
        print(f"item {item}")
        calculator(item)

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
