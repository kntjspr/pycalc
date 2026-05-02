# SORONGON, CHARLES JUVANNE M.

# Distributed Order Processing System
**CS323 - First Laboratory Activity**



---

## Reflection Questions

### 1. How did you distribute orders among worker processes?

Orders were distributed using a **round-robin strategy** through MPI's `comm.send()`. The master process (rank 0) generated 7 orders and assigned each one to a worker using the formula `target = (index % num_workers) + 1`. This spread the orders as evenly as possible across 3 workers. As seen in the output, Worker 1 received 3 orders (ORD-1000, ORD-1003, ORD-1006) while Workers 2 and 3 each received 2 orders — because 7 does not divide evenly among 3 workers. Each worker received its batch as a plain Python list via `comm.recv()`.

### 2. What happens if there are more orders than workers?

When there are more orders than workers, some workers receive more than one order. In the actual run, 7 orders were distributed to 3 workers, so Worker 1 ended up with 3 orders while Workers 2 and 3 got 2 each. Workers handle their extra orders sequentially — they process one order at a time before moving to the next. No orders are dropped or skipped; the round-robin assignment guarantees every order gets assigned to exactly one worker.

### 3. How did processing delays affect the order completion?

The `time.sleep()` call with a random delay between 0.5 and 2.0 seconds caused each order to finish at a different time. Looking at the output, Worker 2 finished first (its longest delay was 1.38s), followed by Worker 3 (longest 1.68s), and finally Worker 1 (longest 1.86s). This is why the worker output lines appeared out of order in the terminal — Workers 2 and 3 both printed their results before Worker 1 even finished its first order. This demonstrates that workers operate independently and concurrently, which is the core benefit of distributed processing.

### 4. How did you implement shared memory, and where was it initialized?

Shared memory was implemented as a plain Python list (`shared_orders = []`) combined with a `threading.Lock()`. Both were initialized inside the `master_process()` function, which runs only on rank 0. Workers do not directly access this structure — instead, they send their completed results back to master via `comm.send()`. The master then receives these results and appends them to `shared_orders` one by one, simulating controlled shared memory access. This approach was necessary on Windows because `multiprocessing.Manager()` objects cannot be serialized and sent across MPI processes.

### 5. What issues occurred when multiple workers wrote to shared memory simultaneously?

In the initial implementation using `multiprocessing.Manager()` and `multiprocessing.Lock()`, two major errors occurred. First, calling `Manager()` at the module level caused a `RuntimeError` about bootstrapping because Windows uses the `spawn` method for new processes, which re-imports the script before the parent process finishes starting. Second, attempting to send the `Lock` object over MPI via `comm.send()` raised a `RuntimeError: Lock objects should only be shared between processes through inheritance` — because OS-level lock handles cannot be pickled and transmitted over a network-style message channel. Without proper synchronization, multiple workers writing to shared memory at the same time would produce incomplete or corrupted entries in the final list.

### 6. How did you ensure consistent results when using multiple processes?

Consistency was ensured through two mechanisms working together. First, MPI's message-passing model (`comm.send` / `comm.recv`) serializes communication between master and workers — each worker sends its results as a complete batch only after finishing all its orders, so no partial writes occur. Second, a `threading.Lock()` wraps every `shared_orders.append()` call on the master side, ensuring that even if results from multiple workers arrive in quick succession, each entry is written atomically. The final output confirmed this worked correctly: all 7 of 7 orders were present, complete, and consistent in the printed list.

---

## Sample Output Summary

```
Workers ran concurrently:
  Worker 2 finished first  (max delay 1.38s)
  Worker 3 finished second (max delay 1.68s)
  Worker 1 finished last   (max delay 1.86s)

Final list: 7/7 orders — complete and consistent
```