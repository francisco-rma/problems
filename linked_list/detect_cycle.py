from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def hasCycle(self) -> bool:
        fast, slow = self, self

        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True

        return False

    def display(self):
        node = self
        i = 0
        while node:
            print(f"index: {i} --- value: {node.val}")
            node = node.next
            i += 1

    def from_list(values: list[int], pos: int):
        head = ListNode(0)
        node = head

        link = None

        for idx, val in enumerate(values):
            node.val = val

            if idx == pos:
                link = node

            if idx < len(values) - 1:
                node.next = ListNode(0)
            else:
                node.next = link

            node = node.next

        return head


def test(values: list[int], pos: int):
    head: ListNode = ListNode.from_list(values, pos)

    if not head.hasCycle():
        head.display()

    else:
        print(f"Cycle detected! Skipping list")

    print("")


test([3, 2, 0, -4], 0)
test([3, 2, 0, -4], 1)
test([3, 2, 0, -4], 2)
test([3, 2, 0, -4], 3)
test([3, 2, 0, -4], -1)
