from __future__ import annotations
import math
import random
from typing import Optional


class HeapNode:
    def __init__(self, val: int, left: Optional[HeapNode] = None, right: Optional[HeapNode] = None):
        self.val: Optional[HeapNode] = val
        self.left: Optional[HeapNode] = left
        self.right: Optional[HeapNode] = right

    def find_insertion_point(values: list[int | None], target: int) -> int:
        h = 0
        while h < int(math.log(len(values), 2)):
            if target < values[h]:
                return h
            elif target < values[2 * h + 1]:
                return 2 * h + 1
            elif target < values[2 * h + 2]:
                return 2 * h + 2
            h = 2 * h + 2

    def heapify(source: list[int], idx: int):
        n = len(source)
        if n == 0 or (idx is not None and idx > n // 2):
            return None

        left_idx = 2 * idx + 1 if 2 * idx + 1 < n else None
        right_idx = 2 * idx + 2 if 2 * idx + 2 < n else None

        node = source[idx]
        left = source[left_idx] if left_idx else float("inf")
        right = source[right_idx] if right_idx else float("inf")

        if node > min([left, right]):
            if left < right:
                source[idx], source[left_idx] = source[left_idx], source[idx]
            else:
                source[idx], source[right_idx] = source[right_idx], source[idx]

        left = source[left_idx] if left_idx else float("-inf")
        right = source[right_idx] if right_idx else float("inf")

        if left > right and right_idx:
            source[left_idx], source[right_idx] = source[right_idx], source[left_idx]

        if left_idx:
            HeapNode.heapify(source, left_idx)
        if right_idx:
            HeapNode.heapify(source, right_idx)

    def build_max_heap(source: list[int]):
        n = len(source)
        for i in range(n // 2, -1, -1):
            HeapNode.heapify(source, i)
        return source


def test(sample: list[int]):
    heap = HeapNode.build_max_heap(sample)

    for i in range(len(heap) // 2):
        print(f"node: {heap[i]}")
        print(f"left: {heap[2 * i + 1]}")
        print(f"right: {heap[2 * i + 2] if (2 * i + 2) < len(heap) else None}")
        print("\n---------\n")
        assert heap[i] <= heap[2 * i + 1]
        if (2 * i + 2) < len(heap):
            assert heap[i] <= heap[2 * i + 2]
    print(heap)


def multi_test():
    population = range(1000)
    i = 0
    while i < 100:
        sample = random.sample(population=population, k=100)
        test(sample=sample)

        i += 1


multi_test()
