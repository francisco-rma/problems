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


def mergeLists(l1: Optional[ListNode], l2: Optional[ListNode]):
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next
        tail.next = None

    while l1:
        tail.next = l1
        l1 = l1.next
        tail = tail.next
        tail.next = None

    while l2:
        tail.next = l2
        l2 = l2.next
        tail = tail.next
        tail.next = None

    return dummy.next


def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:

    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            mergedLists.append(
                mergeLists(lists[i], (lists[i + 1] if i + 1 < len(lists) else None))
            )
        lists = mergedLists

    return lists[0]


source = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
lists = []

for values in source:
    lists.append(ListNode.from_list(values))

result = mergeKLists(lists=lists)

node, i = result, 0

while node:
    print(f"\n index: {i} --- value: {node.val}")
    i += 1
    node = node.next
