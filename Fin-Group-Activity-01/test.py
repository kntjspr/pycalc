import time
from data import generate_data
from parallel_sorting import merge_sort, parallel_merge_sort

if __name__ == "__main__":
    N = 1000000

    data = generate_data(N)

    start = time.time()
    seq_sorted = merge_sort(data.copy())
    end = time.time()
    print("Sequential Time:", end - start)

    start = time.time()
    par_sorted = parallel_merge_sort(data.copy())
    end = time.time()
    print("Parallel Time:", end - start)


    print("Correct:", seq_sorted == par_sorted)