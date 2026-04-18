# Lab Activity 03: Applying Task and Data Parallelism using concurrent.futures

## Questions

### 1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.

Task parallelism involves executing different functions concurrently on the same data. This is demonstrated in the lab when deductions such as **SSS, PhilHealth, Pag-IBIG, and Tax** are calculated simultaneously for a single employee using a `ThreadPoolExecutor`. In contrast, data parallelism focuses on running the same function across different datasets at once. This occurs when the system processes the payroll of **multiple employees** simultaneously using a `ProcessPoolExecutor`. Dividing the workload this way ensures that individual complex records are broken down into smaller tasks while the overall batch of employees is processed across all available CPU cores.

### 2. Explain how concurrent.futures managed execution, including `submit()`, `map()`, and Future objects. Discuss the purpose of with when creating an Executor.

The concurrent.futures module manages concurrency using Executor, `submit()`, `map()`, and Future objects. The submit() function assigns tasks and returns a Future object that stores the result. The map() function applies the same function to multiple employees at the same time. The with statement ensures the executor is properly started and automatically closed after execution.

### 3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did true parallelism occur?

ThreadPoolExecutor uses threads, but Python has a Global Interpreter Lock (GIL) that allows only one thread to run at a time. Because of this, true parallelism does not fully happen for CPU tasks. The threads only run concurrently by switching turns quickly. This means it does not fully use multiple CPU cores.

### 4. Explain why ProcessPoolExecutor enables true parallelism, including memory space separation and GIL behavior.

ProcessPoolExecutor uses separate processes, and each process has its own memory and GIL. This allows multiple processes to run at the same time on different CPU cores. In our code, each employee payroll is computed in a separate process. This results in true parallelism and better performance.

### 5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?

ProcessPoolExecutor scales better if the employees increase to 10,000. This is because the work is divided among multiple CPU cores and processes. Each process handles different employees at the same time. ThreadPoolExecutor is limited by the GIL and is less efficient.

### 6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.

In a real payroll system, Task Parallelism can be used to compute different deductions at the same time for one employee. Data Parallelism can be used to compute payroll for many employees at the same time. ThreadPoolExecutor is used for task parallelism, and ProcessPoolExecutor is used for data parallelism. This makes the payroll system faster and more efficient.