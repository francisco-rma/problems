# =======================================================
# Test harness
# =======================================================

import cProfile
import random
import time
import tracemalloc

import matplotlib.pyplot as plt
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quicksort import quicksort

order = 4
order_delta = 2


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def benchmark(func, source):
    tracemalloc.start()
    start = time.time()
    func(source)
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"{func} execution time:{(end - start):.4f} seconds")
    print(
        f"{func} memory usage: current={current / 1024:.2f} KB, peak={peak / 1024:.2f} KB"
    )
    return end - start, peak


def validity_check():
    """Checks for merge_sort and quick_sort if the resulting array is sorted and contains all original elements."""
    # population = range(-1 * (10 ** (order + 1)), 10 ** (order + 1))
    population = range(-1 * (10 ** (order - 1)), 10 ** (order - 1))
    sizes = range(
        10**order, 10 ** (order + order_delta), 10 ** (order + order_delta - 1)
    )

    quicksort_results = []
    mergesort_results = []

    for i, size in enumerate(sizes):
        print(f"Running test {i + 1} with {size} elements...")
        arr = random.choices(population=population, k=size)

        arr_to_sort = arr.copy()
        start = time.time()
        quicksort(arr_to_sort)
        end = time.time()
        quicksort_results.append((end - start, size))
        assert is_sorted(arr_to_sort)
        print(f"QUCIKSORTed {size} elements in {end - start:.4f} seconds.")

        arr_to_sort = arr.copy()
        start = time.time()
        arr_to_sort = merge_sort(arr_to_sort)
        end = time.time()
        result = end - start
        mergesort_results.append((result, size))
        assert is_sorted(arr_to_sort)
        print(f"MERGESORTed {size} elements in {end - start:.4f} seconds.")
        print("\n" + "=" * 40 + "\n")

    # Plotting results
    sizes_quick = [size for _, size in quicksort_results]
    times_quick = [result for result, _ in quicksort_results]
    sizes_merge = [size for _, size in mergesort_results]
    times_merge = [result for result, _ in mergesort_results]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes_quick, times_quick, marker="o", color="blue", label="Quicksort")
    plt.plot(sizes_merge, times_merge, marker="o", color="red", label="Mergesort")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title("Quicksort vs Mergesort Performance")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# validity_check()

if __name__ == "__main__":
    size = 10**order
    population = range(-1 * (10**order), 10**order)
    arr = random.choices(population=population, k=size)
    print(f"Testing with array of size {size}...")
    print(f"Array: {arr[:5]}")

    cProfile.run("quicksort(arr.copy())")
    cProfile.run("merge_sort(arr.copy())")
    cProfile.run("insertion_sort(arr.copy())")
    cProfile.run("bubble_sort(arr.copy())")

    exec_time, mem_usage = benchmark(quicksort, arr.copy())
    exec_time, mem_usage = benchmark(merge_sort, arr.copy())
    exec_time, mem_usage = benchmark(insertion_sort, arr.copy())
    exec_time, mem_usage = benchmark(bubble_sort, arr.copy())


# =======================================================
# =======================================================
