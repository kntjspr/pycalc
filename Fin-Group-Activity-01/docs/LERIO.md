## Individual Reflection

## Differences Between Sequential and Parallel Execution
The first difference I noticed between sequential and parallel search is how each one goes through the dataset. Sequential linear search is very simple. It just checks each element one by one, starting from index 0, until it finds the target or reaches the end of the list. There is no need for coordination since everything runs in a single flow.
In contrast, the parallel approach divides the dataset into four parts and assigns each part to a different process. These processes run at the same time, each searching its own portion of the data. Once a process finds the target, it sends back the result through a queue, including the correct position in the full dataset.

Because of this setup, the parallel version needs extra handling. Each process must know where its assigned chunk begins in the original dataset. This starting point, or offset, is necessary so the result reflects the correct global index. The sequential version does not deal with this kind of detail at all, since it works on the full dataset directly.


## Performance Behavior Across Dataset Sizes
After testing with small, medium, and large datasets, it became clear that parallelism does not always improve performance.

For the small dataset with 1,000 elements, the sequential search was actually faster. The time spent creating multiple processes, dividing the data, and managing the queue ended up being longer than simply scanning the list from start to finish. This shows that parallel processing comes with overhead that cannot be ignored.

For the medium dataset with 100,000 elements, both approaches performed almost the same. Sometimes the parallel version was slightly faster, but the difference depended on where the target value was located in the list.

With the large dataset of 1,000,000 elements, the parallel version performed noticeably better. This was especially true in worst case situations, such as when the target was near the end or not in the list at all. In these cases, sequential search had to check every element, while the parallel version divided the work among four processes, reducing the total time.

As for sorted and reverse sorted datasets, there was no significant change in performance. Since linear search does not take advantage of ordering, the results were similar to those using random data of the same size.


## Challenges Encountered
One of the most difficult parts of the implementation was calculating the correct global index. Each process only works on a portion of the dataset, so a result like index 5 could refer to different actual positions depending on which process found it. To solve this, I had to make sure each process was given the correct starting index of its chunk and used it when returning results.

Another issue came up when dividing the dataset into chunks. If the total number of elements is not evenly divisible by four, some elements can be left out. I handled this by letting the last process take all remaining elements instead of forcing equal chunk sizes.

Working with the queue also required attention. Since all processes send their results to the same queue, I needed to make sure I collected exactly the expected number of results. After that, I filtered out invalid values to find the correct answer. Missing even one result could lead to incorrect behavior or cause the program to wait indefinitely.


## Insights About Overhead and Synchronization
This activity made it clear that creating processes is not cheap. In Python, each new process involves starting a separate interpreter, copying resources, and setting up communication between processes. This setup takes time, which becomes very noticeable when working with smaller datasets.

On the positive side, synchronization in this task was straightforward. Each process worked independently and only read its assigned data without modifying shared resources. The queue acted as the only point of communication, and since each process only sent one result, there were no conflicts or race conditions. This type of problem is well suited for parallel execution because it requires very little coordination.


## When Parallelism Was Beneficial and When It Wasn't
Parallelism was most useful when working with large datasets, especially in cases where the target value was near the end or not present at all. In these situations, dividing the workload among multiple processes reduced the overall time significantly.

However, for small datasets, parallelism was not helpful and even made things slower. The time needed to create processes and manage communication outweighed the benefits of splitting the task.

From this, I realized that choosing between sequential and parallel execution depends on the situation. Parallelism is not always the better option. Factors like dataset size, overhead cost, and the nature of the task all play a role in deciding which approach is more efficient.