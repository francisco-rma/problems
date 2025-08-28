from __future__ import annotations
from typing import Callable


class Heap:
    def __init__(self, source, order="min"):
        n = len(source)
        self.source = source
        self.order = order

        match self.order:
            case "max":
                self.sift_up: Callable = self._siftup_max
                self.sift_down: Callable = self._siftdown_max
            case "min":
                self.sift_up: Callable = self._siftup_min
                self.sift_down: Callable = self._siftdown_min

        if n == 0:
            return
        for i in range(n // 2, -1, -1):
            self.sift_up(i)

    def __len__(self):
        return len(self.source)

    def __getitem__(self, index):
        return self.source[index]

    def __setitem__(self, index, value):
        self.source[index] = value

    def __iter__(self):
        return iter(self.source)

    def __next__(self):
        return next(self.source)

    def __repr__(self):
        if not self.source:
            return ""

        n = len(self)
        levels = 0

        # Calculate the number of levels in the heap
        while (1 << levels) - 1 < n:
            levels += 1

        max_width = (1 << (levels - 1)) * 3  # Maximum width of the last level
        index = 0
        result = ""
        for level in range(levels):
            level_width = 1 << level  # Number of nodes at this level
            spacing = max_width // (level_width + 1)  # Spacing between nodes
            line = ""

            for i in range(level_width):
                if index >= n:
                    break
                line += f"{' ' * spacing}{self[index]}{' ' * spacing}"
                index += 1

            result += line.center(max_width) + "\n"
        return result

    def _siftdown_min(self, start_idx: int, pos: int) -> int:
        siftee = self[pos]

        while pos > start_idx:
            parent_pos = (pos - 1) >> 1  # (pos - 1) // 2
            parent = self[parent_pos]

            if siftee < parent:
                self[pos] = parent
                pos = parent_pos
                continue

            break

        self[pos] = siftee
        return pos

    def _siftdown_max(self, start_idx: int, pos: int) -> int:
        siftee = self[pos]

        while pos > start_idx:
            parent_pos = (pos - 1) >> 1  # (pos - 1) // 2
            parent = self[parent_pos]

            if siftee > parent:
                self[pos] = parent
                pos = parent_pos
                continue

            break

        self[pos] = siftee
        return pos

    def _siftup_min(self, idx):
        upper_bound = len(self)
        start_idx = idx
        child_idx = 2 * idx + 1
        new_item = self[idx]
        while child_idx < upper_bound:
            sibling_idx = child_idx + 1
            if sibling_idx < upper_bound and self[sibling_idx] < self[child_idx]:
                child_idx = sibling_idx

            self[idx] = self[child_idx]

            idx = child_idx
            child_idx = 2 * idx + 1

        self[idx] = new_item
        self._siftdown_min(start_idx=start_idx, pos=idx)

    def _siftup_max(self, idx):
        upper_bound = len(self)
        start_idx = idx
        child_idx = 2 * idx + 1
        new_item = self[idx]
        while child_idx < upper_bound:
            sibling_idx = child_idx + 1
            if sibling_idx < upper_bound and self[sibling_idx] > self[child_idx]:
                child_idx = sibling_idx

            self[idx] = self[child_idx]

            idx = child_idx
            child_idx = 2 * idx + 1

        self[idx] = new_item
        self._siftdown_max(start_idx=start_idx, pos=idx)

    def _sift_up_early(self, idx):
        upper_bound = len(self)
        start_idx = idx
        child_idx = 2 * idx + 1
        new_item = self[idx]

        while child_idx < upper_bound and not (
            new_item < min(self[child_idx], self[child_idx + 1])
        ):
            sibling_idx = child_idx + 1
            if sibling_idx < upper_bound and self[sibling_idx] < self[child_idx]:
                child_idx = sibling_idx

            self[idx] = self[child_idx]

            idx = child_idx
            child_idx = 2 * idx + 1

        self[idx] = new_item
        self._siftdown_min(start_idx=start_idx, pos=idx)

    def heap_pop(self):
        leaf = self.source.pop()

        if self.source:
            return_item = self[0]
            self[0] = leaf
            self.sift_up(0)
            return return_item

        return leaf

    def heap_pop_early(self):
        leaf = self.source.pop()

        if self.source:
            return_item = self[0]
            self[0] = leaf
            self._sift_up_early(0)
            return return_item

        return leaf

    def heap_push(self, value):
        self.source.append(value)
        return self.sift_down(start_idx=0, pos=len(self) - 1)

    def is_valid(self) -> bool:
        match self.order:
            case "max":
                return self.is_valid_max_heap(self.source)
            case "min":
                return self.is_valid_min_heap(self.source)

    @staticmethod
    def is_valid_min_heap(source: list[int]):
        upper_bound = len(source)
        idx = 0
        node = source[idx]

        while idx < upper_bound:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2

            if left_child_idx < upper_bound:
                break

            assert source[left_child_idx] >= node

            if right_child_idx < upper_bound:
                break

            assert source[right_child_idx] >= node
        return True

    @staticmethod
    def is_valid_max_heap(source: list[int]):
        upper_bound = len(source)
        idx = 0
        node = source[idx]

        while idx < upper_bound:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2

            if left_child_idx < upper_bound:
                break

            assert source[left_child_idx] <= node

            if right_child_idx < upper_bound:
                break

            assert source[right_child_idx] <= node
        return True
