# parallel searching algorithm (assigned member: LERIO)


from multiprocessing import Process, Queue


def worker(sub_data: list, target: int, q: Queue, offset: int) -> None:
    for i in range(len(sub_data)):
        if sub_data[i] == target:
            q.put(offset + i) 
            return
    q.put(None)


def parallel_searching(data: list, target: int) -> int | None:
    num_processes = 4
    chunk_size = len(data) // num_processes
    q = Queue()
    processes = []

    for i in range(num_processes):
        start = i * chunk_size

        if i == num_processes - 1:
            chunk = data[start:]
        else:
            chunk = data[start:start + chunk_size]

        p = Process(target=worker, args=(chunk, target, q, start))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = [q.get() for _ in range(num_processes)]

    found = [r for r in results if r is not None]
    return found[0] if found else None


def main():
    import random

    N = 100000 
    data = [random.randint(1, 1000000) for _ in range(N)]

    element = random.choice(data)   
    non_element = -67             


    print(f"Number we are looking for is: {element}.")
    index1 = parallel_searching(data, element)
    print(f"The number {element} is at index {index1}.")

    print(f"\nNumber we are looking for is: {non_element}.")
    index2 = parallel_searching(data, non_element)

    if index2 is None:
        print(f"The number {non_element} is not on the list.")


if __name__ == "__main__":
    main()