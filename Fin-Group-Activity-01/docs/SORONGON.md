# Fin Group Activity 01: Sequential vs Parallel Algorithms

## Reflection and Analysis

### Differences observed between sequential and parallel execution

In this activity, I discovered that sequential and parallel execution behave extremely differently. Sequential algorithms are straightforward and predictable since they operate in steps utilizing only one process. Parallel algorithms, on the other hand, divide the task into smaller sections that are run concurrently by numerous processes. This complicates parallel execution since it requires process coordination, particularly when merging results.

### Performance behavior across dataset sizes

When I tested different dataset sizes, I discovered that sequential execution was faster for small datasets of 1,000 elements. This is due to the additional overhead associated with parallel execution, such as process creation and communication management. For medium datasets, such as 100,000 items, the performance improved, and parallel was occasionally slightly superior. Parallel execution fared better for large datasets, such as 1,000,000 elements, because the workload was significant enough to benefit from numerous processes running concurrently.

### Challenges encountered during implementation

I encountered various issues during the implementation process. One challenge was accurately breaking the data into parts while ensuring no data was lost. Another problem was ensuring that the results were accurately merged in parallel sorting, as faulty merging can produce false results. Parallel searching also made it difficult to accurately return the global index from several processes. I also found issues relating to multiprocessing, particularly forgetting to utilize the proper structure when running the application.

### Insights about overhead, synchronization, or merging

It taught me that parallel algorithms require extra overhead such as process creation, communication, and synchronization. If the dataset is tiny, these additional stages can cause the program to run slowly. Synchronization is necessary to ensure that all operations complete correctly and do not result in problems such as race situations. Merging findings is also an important stage in parallel sorting because all incomplete results must be integrated into a single accurate output.

### Situations where parallelism was beneficial or unnecessary

Overall, parallelism was useful when working with huge datasets because it lowered execution time by combining numerous processes. However, for small datasets, parallelism was unnecessary and made the process slower due to the additional overhead. This demonstrates that parallel algorithms are not always superior, and the decision between sequential and parallel relies on the size of the task and system resources.



