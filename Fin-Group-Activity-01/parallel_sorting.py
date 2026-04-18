#Sorongon

from multiprocessing import Pool

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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def parallel_merge_sort(data):
    if len(data) <= 1:
        return data

    num_processes = 4
    chunk_size = len(data) // num_processes

    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(merge_sort, chunks)

    while len(sorted_chunks) > 1:
        new_chunks = []

        for i in range(0, len(sorted_chunks), 2):
            if i + 1 < len(sorted_chunks):
                merged = merge(sorted_chunks[i], sorted_chunks[i + 1])
                new_chunks.append(merged)
            else:
                new_chunks.append(sorted_chunks[i])

        sorted_chunks = new_chunks

    return sorted_chunks[0]