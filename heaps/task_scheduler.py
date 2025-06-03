from collections import deque


class TupleHeap:
    def __init__(self, source: list[tuple[str, int]]):
        self.source: list[tuple[str, int]] = source
        self.execution_log: dict[str, int] = {}
        self.task_counter: dict[str, int] = {}

        for task, priority in source:
            if task not in self.task_counter:
                self.task_counter[task] = 0
            self.task_counter[task] += 1

        n = len(source)

        if n == 0:
            return

        for i in range(n // 2, -1, -1):
            self._siftup_min(idx=i)

    def _siftdown_min(self, start_idx: int, pos: int) -> int:
        siftee = self.source[pos]

        while pos > start_idx:
            parent_pos = (pos - 1) >> 1  # (pos - 1) // 2
            parent = self.source[parent_pos]

            if siftee[1] < parent[1] or (
                siftee[1] == parent[1]
                and (self.task_counter[siftee[0]]) > (self.task_counter[parent[0]])
            ):
                self.source[pos] = parent
                pos = parent_pos
                continue
            break

        self.source[pos] = siftee
        return pos

    def _siftup_min(self, idx):
        upper_bound = len(self.source)
        start_idx = idx
        child_idx = 2 * idx + 1
        new_item = self.source[idx]
        while child_idx < upper_bound:
            sibling_idx = child_idx + 1
            if sibling_idx < upper_bound and (
                self.source[sibling_idx][1] < self.source[child_idx][1]
                or (
                    self.source[sibling_idx][1] == self.source[child_idx][1]
                    and (
                        self.task_counter[self.source[sibling_idx][0]]
                        > self.task_counter[self.source[child_idx][0]]
                    )
                )
            ):
                child_idx = sibling_idx

            self.source[idx] = self.source[child_idx]

            idx = child_idx
            child_idx = 2 * idx + 1

        self.source[idx] = new_item
        self._siftdown_min(start_idx=start_idx, pos=idx)

    def heap_pop(self) -> int:
        leaf = self.source.pop()

        if self.source:
            return_item = self.source[0]
            self.source[0] = leaf
            self._siftup_min(idx=0)
            self.task_counter[return_item[0]] = max(self.task_counter[return_item[0]] - 1, 0)
            return return_item

        return leaf

    def heap_push(self, value: tuple[str, int]):
        self.source.append(value)
        if value[0] not in self.task_counter:
            self.task_counter[value[0]] = 0
        self.task_counter[value[0]] += 1
        return self._siftdown_min(start_idx=0, pos=len(self.source) - 1)

    def heap_print(self):
        if not self.source:
            return ""

        n = len(self.source)
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
                line += f"{' ' * spacing}{self.source[index]}{' ' * spacing}"
                index += 1

            result += line.center(max_width) + "\n"
        print(result)


def leastInterval(tasks: list[str], n: int) -> int:
    task_execution_plan = {}
    source = []
    for _, task in enumerate(tasks):
        if task in task_execution_plan:
            task_execution_plan[task] += 1
        else:
            task_execution_plan[task] = 0

        source.append((task, task_execution_plan[task] * n))

    cycle_count = 0

    heap = TupleHeap(source=source)

    task_execution_plan.clear()

    while heap.source:
        task, priority = heap.heap_pop()
        stack = deque()

        while heap.source and cycle_count < priority:
            stack.append((task, priority))
            task, priority = heap.heap_pop()

        while cycle_count < priority:
            cycle_count += 1
            print("Idle")

        cycle_count += 1
        heap.execution_log[task] = cycle_count

        while stack:
            task, priority = stack.pop()
            if cycle_count < priority:
                heap.heap_push((task, priority))
            else:
                cycle_count += 1
                heap.execution_log[task] = cycle_count

    return cycle_count
