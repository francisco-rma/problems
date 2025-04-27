from __future__ import annotations
from typing import Optional


class HeapNode:
    def __init__(self, val: int, left: Optional[HeapNode] = None, right: Optional[HeapNode] = None):
        self.val: Optional[HeapNode] = val
        self.left: Optional[HeapNode] = left
        self.right: Optional[HeapNode] = right

    def max_heapify(source: list[int], idx: int):
        n = len(source)
        if n == 0 or (idx is not None and idx > n // 2):
            return None

        left_idx = 2 * idx + 1 if 2 * idx + 1 < n else None
        right_idx = 2 * idx + 2 if 2 * idx + 2 < n else None

        node = source[idx]
        left = source[left_idx] if left_idx else float("-inf")
        right = source[right_idx] if right_idx else float("-inf")

        if node < max([left, right]):
            if left > right:
                source[idx], source[left_idx] = source[left_idx], source[idx]
            else:
                source[idx], source[right_idx] = source[right_idx], source[idx]

        left = source[left_idx] if left_idx else float("-inf")
        right = source[right_idx] if right_idx else float("inf")

        if left < right and right_idx:
            source[left_idx], source[right_idx] = source[right_idx], source[left_idx]

        if left_idx:
            HeapNode.max_heapify(source, left_idx)
        if right_idx:
            HeapNode.max_heapify(source, right_idx)

    def min_heapify(source: list[int], idx: int):
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
            HeapNode.min_heapify(source, left_idx)
        if right_idx:
            HeapNode.min_heapify(source, right_idx)

    def build_heap(source: list[int], order="max"):
        func = HeapNode.max_heapify if order == "max" else HeapNode.min_heapify
        n = len(source)
        for i in range(n // 2, -1, -1):
            func(source, i)
        return source
