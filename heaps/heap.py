from __future__ import annotations

import random


def max_heapify(source: MaxHeap, idx: int):
    n = source.limit if source.limit is not None else len(source)
    left_idx = (2 * idx) + 1
    right_idx = (2 * idx) + 2
    target_idx = right_idx

    if left_idx < n and source[left_idx] > source[idx]:
        target_idx = left_idx
    else:
        target_idx = idx

    if right_idx < n and source[right_idx] > source[target_idx]:
        target_idx = right_idx

    if target_idx != idx:
        source[idx], source[target_idx] = source[target_idx], source[idx]
        max_heapify(source, target_idx)

    return


class MaxHeap:
    def __init__(self, source, limit=None):
        n = len(source)
        self.limit: int | None = limit
        self.source: list[int] = source

        if n == 0:
            return

        for i in range(n // 2, -1, -1):
            max_heapify(self, i)
            # self.sift_up(i)

        if self.limit is not None and len(self.source) > self.limit:
            result = []
            i = 0
            while i < self.limit:
                result.append(self.heap_pop())
                i += 1

            self.source = result

    def __len__(self):
        return len(self.source)

    def __getitem__(self, index):
        if index is None:
            raise ValueError(f"Index is {index}")
        if index >= len(self):
            raise IndexError("Index out of bounds")
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

    def heap_pop(self):
        leaf = self.source.pop()

        if self.source:
            return_item = self[0]
            self[0] = leaf
            self.sift_up(0)
            return return_item

        return leaf

    def heap_push(self, value):
        if self.limit is not None:
            assert len(self.source) <= self.limit
            if len(self.source) == self.limit:
                min_idx = self.find_min_idx()
                self[min_idx], self[-1] = self[-1], self[min_idx]
                self.sift_down(start_idx=0, pos=min_idx)
                self.source.pop()

        self.source.append(value)
        result = self.sift_down(start_idx=0, pos=len(self) - 1)
        assert self.is_valid()
        return result

    def sift_down(self, start_idx: int, pos: int) -> int:
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

    def sift_up(self, idx: int):
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
        self.sift_down(start_idx=start_idx, pos=idx)

    def find_min_idx(self):
        min = float("+inf")
        min_idx = None
        for idx, value in enumerate(self):
            if value[1] < min:
                min = value[1]
                min_idx = idx
        return min_idx

    def is_valid(self) -> bool:
        upper_bound = len(self.source)
        if upper_bound <= 0:
            return True
        idx = 0
        node = self.source[idx]

        while idx < upper_bound // 2:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2

            if left_child_idx >= upper_bound:
                break

            assert self.source[left_child_idx] <= node

            if right_child_idx >= upper_bound:
                break

            assert self.source[right_child_idx] <= node

            idx += 1

        return True


class MinHeap:
    def __init__(self, source, limit=None):
        n = len(source)
        self.source = source
        self.limit = limit

        if n == 0:
            return
        for i in range(n // 2, -1, -1):
            self.sift_up(i)

        if self.limit is not None and len(self.source) > self.limit:
            result = []
            i = 0
            while i < self.limit:
                result.append(self.heap_pop())
                i += 1

            self.source = result

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

    def heap_pop(self):
        leaf = self.source.pop()

        if self.source:
            return_item = self[0]
            self[0] = leaf
            self.sift_up(0)
            return return_item

        return leaf

    def heap_push(self, value):
        if self.limit is not None:
            assert len(self.source) <= self.limit
            if len(self.source) == self.limit:
                max_idx = self.find_max_idx()
                self[max_idx], self[-1] = self[-1], self[max_idx]
                self.sift_down(start_idx=0, pos=max_idx)
                self.source.pop()
        self.source.append(value)
        return self.sift_down(start_idx=0, pos=len(self) - 1)

    def sift_down(self, start_idx: int, pos: int) -> int:
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

    def sift_up(self, idx):
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
        self.sift_down(start_idx=start_idx, pos=idx)

    def find_max_idx(self):
        max = float("-inf")
        max_idx = None
        for idx, value in enumerate(self):
            if isinstance(value, list):
                value = value[1]
            if value > max:
                max = value
                max_idx = idx
        return max_idx

    def is_valid(self) -> bool:
        upper_bound = len(self.source)
        if upper_bound <= 0:
            return True

        idx = 0
        node = self.source[idx]

        while idx < upper_bound // 2:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2

            if left_child_idx >= upper_bound:
                break

            assert self.source[left_child_idx] >= node

            if right_child_idx >= upper_bound:
                break

            assert self.source[right_child_idx] >= node

            idx += 1

        return True


if __name__ == "__main__":
    source = random.sample(population=range(100), k=10)
    print(source)
    hp = MaxHeap(source, limit=len(source))
    print(hp.source)
    print(hp)
