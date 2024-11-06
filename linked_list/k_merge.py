from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def from_list(values: list[int]):
        head = None
        result = None
        for item in values:
            if not result:
                result = ListNode(val=item)
                head = result
            else:
                result.next = ListNode(val=item)
                result = result.next

        return head


def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    result = None

    min_val = None
    min_idx = None
    tracker: dict[int, ListNode] = {}

    for idx, node in enumerate(lists):
        if not node:
            continue
        print(node, node.val)
        tracker[idx] = node

        if not min_val:
            min_val = node.val
            min_idx = idx
            continue

        if node.val < min_val:
            min_val = node.val
            min_idx = idx

    result = ListNode(min_val)
    tracker[min_idx] = tracker[min_idx].next
    result_tail = result

    while tracker.keys():
        for i in range(len(lists)):
            if i not in tracker:
                continue

            node = tracker[i]

            if not node:
                tracker.pop(i)
                continue

            if not min_val:
                min_val = node.val
                min_idx = i

            if node.val == result_tail.val:
                min_val = node.val
                min_idx = i
                break
            elif node.val < min_val:
                min_val = node.val
                min_idx = i

        result_tail.next = ListNode(min_val)
        if min_idx in tracker:
            tracker[min_idx] = tracker[min_idx].next
        result_tail = result_tail.next
        min_val = None

    return result


source = [[1, 2, 4], [1, 3, 5], [3, 6]]
lists = []

for values in source:
    lists.append(ListNode.from_list(values))

result = mergeKLists(lists=lists)

node, i = result, 0

while node:
    print(f"\n index: {i} --- value: {node.val}")
    i += 1
    node = node.next
