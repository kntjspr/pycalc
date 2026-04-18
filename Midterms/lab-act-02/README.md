# Lab Activity 02: Multithreading vs Multiprocessing

## Questions

### 1. Which approach demonstrates true parallelism in Python? Explain.

Multiprocessing demonstrates true parallelism. Each process gets its own Python interpreter and memory space, allowing them to run simultaneously on different CPU cores. Threads in Python are limited by GIL, which only allows one thread to execute Python bytecode at a time, even on multi-core systems.

### 2. Compare execution times between multithreading and multiprocessing.

Based on our benchmark results:

| Technique       | Time (s)  |
|-----------------|-----------|
| Multiprocessing | ~0.073    |
| Multithreading  | ~0.001    |

Multithreading is significantly faster for this workload because:
- Thread creation has minimal overhead (shared memory space)
- Process creation requires spawning a new interpreter and copying memory
- The actual computation (GWA calculation) is trivial and completes almost instantly

### 3. Can Python handle true parallelism using threads? Why or why not?

No, Python cannot achieve true parallelism with threads for CPU-bound tasks. The GIL prevents multiple threads from executing Python bytecode simultaneously. This is a CPython implementation detail designed to simplify memory management. While threads can run concurrently (taking turns), they cannot run in parallel on multiple cores for CPU-intensive work.

However, threads can achieve parallelism for I/O-bound tasks since the GIL is released during I/O operations (file reads, network requests, etc.).

### 4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?

Heavy benchmark results (1000 grades):

| Technique       | Time (s)  |
|-----------------|-----------|
| Multiprocessing | ~2.242    |
| Multithreading  | ~0.097    |


- Multithreading remains faster because the computation itself is still lightweight (simple arithmetic)
- Multiprocessing overhead becomes even more apparent as we spawn 1000 processes
- The GIL doesn't hurt us here because each thread's work is not needed

In short, for truly CPU-intensive tasks (like computing millions of iterations per grade), multiprocessing would eventually win because it can utilize multiple CPU cores. But for simple arithmetic, the process creation overhead dominates.

### 5. Which method is better for CPU-bound tasks and which for I/O-bound tasks?

| Task Type | Best Method | Reason |
|-----------|-------------|--------|
| CPU-bound | Multiprocessing | Bypasses GIL, uses multiple cores |
| I/O-bound | Multithreading | Lower overhead, GIL released during I/O |

Examples:
- CPU-bound: Image processing, mathematical computations, data compression
- I/O-bound: Web scraping, file operations, database queries, API calls

### 6. How did your group apply creative coding or algorithmic solutions in this lab?

1. We created a benchmark script that spawns both implementations as subprocesses with identical inputs, parses their output, and compares execution times automatically.

2. We used fixed input data to ensure fair comparison between the two approaches.

3. We added a separate benchmark `benchmark_heavy.py` that tests with 1000 grades and includes CPU-intensive work to demonstrate when multiprocessing actually becomes beneficial.

4. We fixed the previous given script where it calculates each grade's individually resulting it in dividing by 1. Input is singular and therefore it does `input/len(input)` resulting a input divided by 1.

## Files

- `multithreading.py` - GWA calculator using threads
- `multiprocessing_gwa.py` - GWA calculator using processes
- `benchmark.py` - Quick comparison with 5 grades
- `benchmark_heavy.py` - Stress test with 1000 grades
