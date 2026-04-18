#SISI

import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    data = random.sample(range(1, 100_001), 10_000)

    start = time.perf_counter()
    result = merge_sort(data[:])
    elapsed = time.perf_counter() - start

    print(f"sequential merge sort:")
    print(f"input size:   {len(data):,} elements")
    print(f"time:         {elapsed:.4f}s")
    print(f"correct:      {result == sorted(data)}")
    print(f"first 10:     {result[:10]}")
