# =======================================================
# Test harness
# =======================================================


# =======================================================
# Heapify
# =======================================================

import random
from collections import namedtuple
import time
from typing import NamedTuple
from heap import Heap
import csv


def test_max_heap(sample: list[int]):
    max_val = max(sample)
    heap = Heap(sample, order="max")

    for i in range(len(heap) // 2):
        assert heap[0] == max_val
        assert heap[i] >= heap[2 * i]
        if (2 * i + 2) < len(heap):
            assert heap[i] >= heap[2 * i + 2]


def test_min_heap(sample: list[int]):
    min_val = min(sample)
    heap = Heap(sample, order="min")

    for i in range(len(heap) // 2):
        assert heap[0] == min_val
        assert heap[i] <= heap[2 * i]
        if (2 * i + 2) < len(heap):
            assert heap[i] <= heap[2 * i + 2]


def multi_test():
    population = range(1000)
    i = 0
    while i < 100:
        sample = random.sample(population=population, k=random.randint(50, 500))
        heap = Heap(source=sample)
        # print(f"MIN: {min(sample)} - MAX: {max(sample)}\n")

        test_max_heap(sample=heap)
        # print(f"Max heap start: {heap[0]}")
        # print(f"Max heap end: {heap[-1]}")

        test_min_heap(sample=heap)
        # print(f"Min heap start: {heap[0]}")
        # print(f"Min heap end: {heap[-1]}")

        # print("\n---------\n")

        i += 1
        # print(heap)


def heap_pop_test():
    sample = random.sample(population=range(10**6), k=10**5)
    control = sorted(sample)

    heap = Heap(source=sample, order="min")

    while heap and control:
        result = heap.heap_pop()
        control_result = control.pop(0)
        assert result == control_result
        assert len(heap) == len(control)
        # print(heap)
        # print(f"{result} has been popped!\n")
        # print(heap)
        # print("\n---------\n")


def heap_push_test():
    control = random.sample(population=range(10**6), k=10**5)
    heap = Heap(source=[], order="min")

    i = 0
    while len(heap) < len(control):
        idx = heap.heap_push(control[i])
        assert heap[idx] == control[i]
        assert len(heap) == len(control[: i + 1])

        # print(f"{heap[idx]} has been pushed to index {idx}!\n")
        # print(heap)
        # print("\n---------\n")

        i += 1


def stream_test():
    sample = random.sample(population=range(10**6), k=10**5)
    heap = Heap(source=sample.copy(), order="min")

    stream = [random.randint(0, 100) for _ in range(len(heap))]

    for i, instruction in enumerate(stream):
        if len(heap) == 0 or instruction % 2 != 0:
            cur_size = len(heap)
            idx = heap.heap_push(stream[i])
            assert heap[idx] == stream[i]
            assert len(heap) == cur_size + 1
        else:
            cur_size = len(heap)
            result = heap.heap_pop()
            assert result <= heap[0]
            assert len(heap) == cur_size - 1


def multi_heap_pop_test():
    population = range(10**6, 10**7)
    i = 0
    Result: NamedTuple = namedtuple("Results", ["size", "range", "time", "early_return"])

    results = []
    while i < 10**2:
        size = 10**5

        sample = random.sample(population=population, k=size)
        early_sample = sample.copy()

        heap = Heap(source=sample)
        early_heap = Heap(source=early_sample)

        start = time.time()
        while heap:
            heap.heap_pop()
        end = time.time()

        results.append(
            Result(size=size, range=population[-1], time=end - start, early_return=False)
        )
        print(f"{i} - {size} - {end - start:.6f} seconds")

        start = time.time()
        while early_heap:
            early_heap.heap_pop()
        end = time.time()

        results.append(Result(size=size, range=population[-1], time=end - start, early_return=True))
        print(f"{i} - {size} - {end - start:.6f} seconds")

        i += 1

    with open("results.csv", "w", newline="") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=Result._fields)
        csv_writer.writeheader()
        for result in results:
            csv_writer.writerow(result._asdict())


heap_push_test()
heap_pop_test()
stream_test()
multi_heap_pop_test()
