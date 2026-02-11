import datetime
import multiprocessing

from cpu_loaders.calculator import calculator

if __name__ == "__main__":
    start = datetime.datetime.now()

    processes = []
    for thread in range(10):
        process = multiprocessing.Process(target=calculator, kwargs={"item_nr": thread})
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
