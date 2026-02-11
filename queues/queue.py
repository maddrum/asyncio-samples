import asyncio
import datetime
import signal

from coroutines.coroutines import my_routine

item = 0


async def producer(queue: asyncio.Queue, shutdown_event: asyncio.Event):
    global item
    while True:
        if shutdown_event.is_set():
            print("Producer cancelled")
            break

        await queue.put(item)

        print(f"Just put item: {item}")
        item += 1


async def consumer(queue: asyncio.Queue, producer_task: asyncio.Task):
    while True:
        if producer_task.done() and queue.empty():
            print("Producer stopped - cancelling consumer")
            break
        item = await queue.get()
        print(f"Just got item: {item}")
        await my_routine(item)


async def main():
    queue = asyncio.Queue(maxsize=5)
    shutdown_event = asyncio.Event()

    def signal_handler():
        if not shutdown_event.is_set():
            print("\nKeyboard interrupt detected. Starting graceful shutdown...")
            shutdown_event.set()
        else:
            print("\nShutdown already in progress. Please wait for buffers to empty...")

    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, signal_handler)

    producer_task = asyncio.create_task(producer(queue, shutdown_event))
    consumer_task = asyncio.create_task(consumer(queue, producer_task))

    await asyncio.gather(
        producer_task,
        consumer_task,
    )


if __name__ == "__main__":
    start = datetime.datetime.now()

    asyncio.run(main())

    end = datetime.datetime.now()
    print("=" * 20)
    print(f"Total time: {end - start}")
