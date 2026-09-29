# Asyncio Samples

A collection of small runnable demos comparing synchronous, `asyncio`,
threading, and multiprocessing approaches for I/O-bound and CPU-bound
workloads. Run any sample directly:

```bash
python -m <package>.<module>   # e.g. python -m gatherer.gatherer_routine
# or
python <path>/<file>.py        # e.g. python synced.py
```

Most samples print a `Total time:` so you can compare approaches directly.

## Shared building blocks

- `cpu_loaders/calculator.py` — CPU-bound workloads: `calculator` (50M sqrt
  iterations) and `heavy_calculator` (500M). Used by all CPU demos.
- `coroutines/coroutines.py` — coroutine library used by the tasks/gatherer/
  queues samples:
  - `async_calculator` — wraps the blocking `calculator` in a coroutine
    (still blocks the event loop — async does NOT speed up CPU work).
  - `my_routine` / `my_subroutine` — sleep 1-5s, simulating async I/O.
  - `*_no_wait` variants — same but with no awaits, finish instantly.
- `sync_to_async/waiter.py` — `synced_wait`, a blocking `time.sleep` loop
  simulating a synchronous I/O call (e.g. a sync HTTP request).
- `tasks/common.py` — `update_set_state`, a done-callback that discards
  finished tasks from a tracking set.
- `synced.py` — baseline: runs `calculator` 10 times sequentially
  (slowest variant, reference point).

## Samples

### `tasks/` — `asyncio.create_task` basics

- `tasks_single_routine.py` — minimal `create_task` + `await` demo.
  `create_task` returns immediately; you must await or the task may be
  killed at shutdown.
- `tasks_coroutines.py` — schedules 10 sleeping routines as tasks, tracks
  them in a set, and awaits `asyncio.wait` each iteration so tasks aren't
  killed mid-sleep.
- `tasks_coroutines_no_wait.py` — same structure but the routines never
  sleep, so tasks finish instantly with no explicit wait.
- `tasks_calculator.py` — tasks over CPU-bound coroutines: proves tasks
  alone do NOT parallelize CPU work (event loop is blocked by each task).

### `gatherer/` — `asyncio.gather`

- `gatherer_routine.py` — gathers 10 sleeping routines; they run
  concurrently, total time ≈ max sleep, not the sum. `gather` blocks
  until everything finishes.
- `gatherer_calculator.py` — gathers 10 CPU-bound coroutines; still
  sequential because each one blocks the loop.

### `sync_to_async/` — calling blocking sync code from async code

- `synced_thread_block.py` — anti-pattern: an `async def` that calls the
  blocking `synced_wait` directly. The event loop freezes; 10 items take
  ~100s total.
- `synced_thread_no_block.py` — correct fix: `asyncio.to_thread(synced_wait, item)`
  offloads the blocking call to a worker thread; items run concurrently
  (~10s). NOTE: `to_thread` needs a *sync* callable — passing a coroutine
  function produces "coroutine was never awaited".

### `process_pool/` — real CPU parallelism

- `pure_multithreaded.py` — raw `multiprocessing.Process` workers
  (despite the name, these are processes — they bypass the GIL).
- `real_async.py` — `ProcessPoolExecutor` + `loop.run_in_executor`: the
  correct way to run CPU-bound work from async code.
- `synced.py` — anti-pattern: pool is created but `calculator` is called
  inline, so it runs sequentially on the event loop thread.

### `queues/` — producer/consumer

- `queue.py` — `asyncio.Queue(maxsize=5)` producer/consumer demo with
  graceful shutdown: Ctrl+C sets an event, the producer stops, and the
  consumer drains the queue before exiting.

## Key takeaways

- `async`/`await` helps only with **I/O-bound** work.
- CPU-bound work needs **processes** (`ProcessPoolExecutor` /
  `multiprocessing`), never bare coroutines.
- Blocking sync calls inside coroutines freeze the event loop — use
  `asyncio.to_thread` (sync callable only).
- Always `await`/`gather`/`join` scheduled work, or it may be cancelled
  on shutdown.
