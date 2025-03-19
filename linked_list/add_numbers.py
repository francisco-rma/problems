from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int, next: ListNode = None):
        self.val = val
        self.next = next
        pass

    def parse_int(self):
        digits = []
        node = self

        while node is not None:
            digits.append(node.val)
            node = node.next

        result = 0
        order = 0

        for value in digits:
            result += int(value) * (10**order)
            order += 1

        return result

    def from_list(self, values: list[int]):
        node = self
        for idx, val in enumerate(values):
            node.val = val

            if idx < len(values) - 1:
                node.next = ListNode(0)

            node = node.next

    def from_number(value: int):
        digits = str(value)
        node = None

        for digit in digits:
            new_node = ListNode(int(digit), next=node)
            new_node.next = node
            node = new_node

        return node

    def addTwoNumbers(
        l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        a = l1.parse_int()
        b = l2.parse_int()

        return a + b

    def display(self):
        node = self
        i = 0
        while node:
            print(f"index: {i} --- value: {node.val}")
            node = node.next
            i += 1


l1_source = [1, 2, 3]
l2_source = [4, 5, 6]

l1, l2 = ListNode(0), ListNode(0)

l1.from_list(l1_source)
l2.from_list(l2_source)

result = ListNode.addTwoNumbers(l1=l1, l2=l2)

print(result)

result: ListNode = ListNode.from_number(result)
result.display()
