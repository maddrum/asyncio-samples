"""Shared blocking workload: a plain synchronous function that sleeps.

Used by the sync_to_async samples to simulate a blocking I/O call
(e.g. a sync HTTP request or DB query) inside async code.
"""

import time


def synced_wait(item):
    """Block the calling thread for 10 seconds, printing progress each second.

    :param item: identifier printed in the log messages
    """
    for _item in range(10):
        time.sleep(1)
        print(f"task item sleeper {item}")
        print(f'slept for {_item} s')
