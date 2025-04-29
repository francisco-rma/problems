from __future__ import annotations


class Heap:
    def build_heap(source: list[int], order="max"):
        func = Heap.max_heapify if order == "max" else Heap.min_heapify
        n = len(source)
        for i in range(n // 2, -1, -1):
            func(source, i)
        return source

    def __init__(self, source: list[int], order="max"):
        Heap.build_heap(source, order=order)
        self.source = source

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

    def max_heapify(self, idx: int):
        n = len(self)
        if n == 0 or (idx is not None and idx > n // 2):
            return None

        left_idx = 2 * idx + 1 if 2 * idx + 1 < n else None
        right_idx = 2 * idx + 2 if 2 * idx + 2 < n else None

        node = self[idx]

        if node is None:
            return None

        left = self[left_idx] if left_idx and self[left_idx] else float("-inf")
        right = self[right_idx] if right_idx and self[right_idx] else float("-inf")

        if node < max(left, right):
            if left > right:
                self[idx], self[left_idx] = self[left_idx], self[idx]
            else:
                self[idx], self[right_idx] = self[right_idx], self[idx]

        left = self[left_idx] if left_idx and self[left_idx] else float("-inf")
        right = self[right_idx] if right_idx and self[right_idx] else float("inf")

        if left < right and right_idx:
            self[left_idx], self[right_idx] = (
                self[right_idx],
                self[left_idx],
            )

        if left_idx:
            Heap.max_heapify(self, left_idx)
        if right_idx:
            Heap.max_heapify(self, right_idx)

    def min_heapify(self, idx: int):
        n = len(self)
        if n == 0 or (idx is not None and idx > n // 2):
            return None

        left_idx = 2 * idx + 1 if 2 * idx + 1 < n else None
        right_idx = 2 * idx + 2 if 2 * idx + 2 < n else None

        node = self[idx]
        left = self[left_idx] if left_idx else float("inf")
        right = self[right_idx] if right_idx else float("inf")

        if node > min([left, right]):
            if left < right:
                self[idx], self[left_idx] = self[left_idx], self[idx]
            else:
                self[idx], self[right_idx] = self[right_idx], self[idx]

        left = self[left_idx] if left_idx else float("-inf")
        right = self[right_idx] if right_idx else float("inf")

        if left > right and right_idx:
            self[left_idx], self[right_idx] = (
                self[right_idx],
                self[left_idx],
            )

        if left_idx:
            Heap.min_heapify(self, left_idx)
        if right_idx:
            Heap.min_heapify(self, right_idx)

    def _sift_down(self, start_idx: int, pos: int):
        siftee = self[pos]

        while pos > start_idx:
            parent_pos = (pos - 1) // 2
            parent_pos_control = (pos - 1) >> 1
            assert parent_pos == parent_pos_control

            parent = self[parent_pos]

            if siftee < parent:
                self[pos] = parent
                pos = parent_pos
                continue

            break

        self[pos] = siftee

    def _sift_up(self, idx):
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
        self._sift_down(start_idx=start_idx, pos=idx)

    def heap_pop(self) -> int:
        result = self.source.pop()

        if self.source:
            return_item = self[0]
            self[0] = result
            self._sift_up(0)
            return return_item

        return result
