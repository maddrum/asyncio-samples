"""Producer/consumer pattern with asyncio.Queue + graceful SIGINT shutdown.

- producer: puts incrementing items into a bounded queue (maxsize=5)
- consumer: processes items via `my_routine` (simulated async I/O)
- Ctrl+C sets a shutdown event; producer stops, consumer drains the
  queue and exits when it is empty.
"""

import asyncio
import datetime
import signal

from coroutines.coroutines import my_routine

# Global counter of produced items (shared state for the demo).
item = 0


async def producer(queue: asyncio.Queue, shutdown_event: asyncio.Event):
    """Put incrementing items into the queue until shutdown is signaled.

    Blocks on `queue.put` when the queue is full (backpressure).

    :param queue: bounded queue shared with the consumer
    :param shutdown_event: set by the SIGINT handler to stop producing
    """
    global item
    while True:
        if shutdown_event.is_set():
            print("Producer cancelled")
            break

        await queue.put(item)

        print(f"Just put item: {item}")
        item += 1


async def consumer(queue: asyncio.Queue, producer_task: asyncio.Task):
    """Consume items until the producer finishes AND the queue is empty.

    :param queue: bounded queue shared with the producer
    :param producer_task: producer task, checked to detect completion
    """
    while True:
        if producer_task.done() and queue.empty():
            print("Producer stopped - cancelling consumer")
            break
        item = await queue.get()
        print(f"Just got item: {item}")
        # Process the item with simulated async I/O work.
        await my_routine(item)


async def main():
    """Wire up queue, producer, consumer, and the SIGINT handler."""
    queue = asyncio.Queue(maxsize=5)
    shutdown_event = asyncio.Event()

    # Ctrl+C -> set the event; producer exits, consumer drains leftovers.
    def signal_handler():
        if not shutdown_event.is_set():
            print("\nKeyboard interrupt detected. Starting graceful shutdown...")
            shutdown_event.set()
        else:
            print("\nShutdown already in progress. Please wait for buffers to empty...")

    # Asyncio-aware signal handling (safe alternative to signal.signal).
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
