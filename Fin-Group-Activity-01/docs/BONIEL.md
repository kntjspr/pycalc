## Individual reflection (Boniel)


Based on my observation with the sequential and parallel execution, I can clearly say without a doubt that the parallel execution is way faster compared to the sequential. Especially sinceI have a potato laptop, I can clearly notice the time difference between the two.

Now, as for the performance behavior across the different dataset sizes, on small dataset, on sequential it was not that very noticeable at least not on what I've noticed on searching but it was on the sorting side. Compared to the parallel on small dataset,
I've noticed the difference but not that huge of a gap, very subtle only. BUT on the medium and Large datasets, that's where i can notice the clear difference in terms of time execution between the sequential and the parallel; parallel was way faster. So, I say that the larger the dataset the faster it is to opt for a parallel algorithm instead of a traditional sequential or linear approach.


As for the challenges encountered during implementation, I was assigned on sequential searching, so not that much of a problem. In fact the challenge that I've faced is more on decision-making on what to name the variable or should I just straight up return an f-string or just put it on the main function. Those kind of things.
But on testing, I only suggested on how to do it but not on how it is implemented. Also just watched the end-result (demonstration).


As for overhead, synchronization, and merging, I realized that parallel is not always instantly faster because there are extra steps involved like dividing the data and combining the results after. These steps add overhead and can affect performance. There is also synchronization where processes need to coordinate, which can slow things down if not handled properly.

Because of that, parallelism is not always necessary. For small datasets or simple tasks, sequential is actually more efficient since it is simpler and has no overhead (I actually like it simple). But for larger datasets, parallel becomes more beneficial because it can process multiple parts at the same time. So overall, choosing between sequential and parallel depends on the problem and dataset size, not just speed alone.


