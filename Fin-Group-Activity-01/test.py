import random
import statistics
import time

from data import generate_data
from parallel_sorting import merge_sort as parallel_module_merge_sort
from parallel_sorting import parallel_merge_sort
from parallel_searching import parallel_searching
from sequential_searching import sequential_searching
from sequential_sort import merge_sort as sequential_merge_sort

SEED = 42
SIZES = [1000, 10000, 100000]
RUNS = 3


def benchmark_sort(name, fn, input_data, expected, runs):
    times = []
    is_correct = True

    for _ in range(runs):
        data_copy = input_data.copy()
        start = time.perf_counter()
        result = fn(data_copy)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

        if result != expected:
            is_correct = False

    return {
        "name": name,
        "avg": statistics.mean(times),
        "min": min(times),
        "max": max(times),
        "correct": is_correct,
    }


def benchmark_search(name, fn, input_data, target, expected, runs):
    times = []
    is_correct = True

    for _ in range(runs):
        start = time.perf_counter()
        result = fn(input_data, target)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

        if result != expected:
            is_correct = False

    return {
        "name": name,
        "avg": statistics.mean(times),
        "min": min(times),
        "max": max(times),
        "correct": is_correct,
    }


def print_results(title, results):
    print(f"\n{title}")
    print("-" * len(title))
    print(f"{'Algorithm':45} {'Avg (s)':>10} {'Min (s)':>10} {'Max (s)':>10} {'Correct':>10}")
    for row in results:
        print(
            f"{row['name']:45} "
            f"{row['avg']:10.6f} "
            f"{row['min']:10.6f} "
            f"{row['max']:10.6f} "
            f"{str(row['correct']):>10}"
        )


def main():
    random.seed(SEED)
    print(f"Fixed benchmark config: seed={SEED}, runs={RUNS}, sizes={SIZES}")

    for size in SIZES:
        print(f"\n=== Input Size: {size:,} ===")
        data = generate_data(size)

        expected_sorted = sorted(data)
        sort_results = [
            benchmark_sort(
                "sequential_sort.merge_sort",
                sequential_merge_sort,
                data,
                expected_sorted,
                RUNS,
            ),
            benchmark_sort(
                "parallel_sorting.merge_sort",
                parallel_module_merge_sort,
                data,
                expected_sorted,
                RUNS,
            ),
            benchmark_sort(
                "parallel_sorting.parallel_merge_sort",
                parallel_merge_sort,
                data,
                expected_sorted,
                RUNS,
            ),
        ]
        print_results("Sorting Benchmarks", sort_results)

        present_target = random.choice(data)
        absent_target = -1
        expected_present_index = data.index(present_target)

        search_results = [
            benchmark_search(
                "sequential_searching (present element)",
                sequential_searching,
                data,
                present_target,
                expected_present_index,
                RUNS,
            ),
            benchmark_search(
                "sequential_searching (absent element)",
                sequential_searching,
                data,
                absent_target,
                None,
                RUNS,
            ),
            benchmark_search(
                "parallel_searching (present element)",
                parallel_searching,
                data,
                present_target,
                expected_present_index,
                RUNS,
            ),
            benchmark_search(
                "parallel_searching (absent element)",
                parallel_searching,
                data,
                absent_target,
                None,
                RUNS,
            ),
        ]
        print_results("Searching Benchmarks", search_results)


if __name__ == "__main__":
    main()