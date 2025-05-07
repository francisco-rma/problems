from collections import deque


def _siftdown_min(source: list[tuple[str, int]], start_idx: int, pos: int) -> int:
    siftee = source[pos]

    while pos > start_idx:
        parent_pos = (pos - 1) >> 1  # (pos - 1) // 2
        parent = source[parent_pos]

        if siftee[1] < parent[1] or (siftee[1] == parent[1] and ord(siftee[0]) < ord(parent[0])):
            source[pos] = parent
            pos = parent_pos
            continue
        break

    source[pos] = siftee
    return pos


def _siftup_min(source: list[int], idx):
    upper_bound = len(source)
    start_idx = idx
    child_idx = 2 * idx + 1
    new_item = source[idx]
    while child_idx < upper_bound:
        sibling_idx = child_idx + 1
        if sibling_idx < upper_bound and (
            source[sibling_idx][1] < source[child_idx][1]
            or (
                source[sibling_idx][1] == source[child_idx][1]
                and ord(source[sibling_idx][0]) < ord(source[child_idx][0])
            )
        ):
            child_idx = sibling_idx

        source[idx] = source[child_idx]

        idx = child_idx
        child_idx = 2 * idx + 1

    source[idx] = new_item
    _siftdown_min(source=source, start_idx=start_idx, pos=idx)


def heap_pop(source: list[tuple[str, int]]) -> int:
    leaf = source.pop()

    if source:
        return_item = source[0]
        source[0] = leaf
        _siftup_min(source=source, idx=0)
        return return_item

    return leaf


def heapify(source: list[tuple[str, int]]):
    n = len(source)

    if n == 0:
        return

    for i in range(n // 2, -1, -1):
        _siftup_min(source=source, idx=i)


def heap_push(source: list[tuple[str, int]], value: tuple[str, int]):
    source.append(value)
    return _siftdown_min(source=source, start_idx=0, pos=len(source) - 1)


def heap_print(source: list[tuple[str, int]]):
    if not source:
        return ""

    n = len(source)
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
            line += f"{' ' * spacing}{source[index]}{' ' * spacing}"
            index += 1

        result += line.center(max_width) + "\n"
    print(result)


def leastInterval(tasks: list[str], n: int) -> int:
    task_execution_plan = {}
    source = []
    base = 0
    for _, task in enumerate(tasks):
        if task in task_execution_plan:
            task_execution_plan[task] += 1
        else:
            task_execution_plan[task] = 0

        source.append((task, base + task_execution_plan[task] * n))
        base += 1

    cycle_count = 0

    heapify(source=source)

    task_execution_plan.clear()

    while source:
        heap_print(source)
        task, priority = heap_pop(source=source)

        if task not in task_execution_plan:
            cycle_count += 1
            task_execution_plan[task] = cycle_count
            continue

        stack = deque()

        while (
            source and task in task_execution_plan and cycle_count - task_execution_plan[task] < n
        ):
            stack.append((task, priority))
            task, priority = heap_pop(source=source)

        while stack:
            heap_push(source=source, value=stack.pop())

        if task in task_execution_plan and cycle_count - task_execution_plan[task] < n:
            heap_push(source=source, value=(task, priority))
            cycle_count += 1
            print("Idle")
            continue

        cycle_count += 1
        task_execution_plan[task] = cycle_count

    return cycle_count
