from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def find(self, target: int):
        val = self

        while val:
            if val.val == target:
                return val
            val = val.next

    def get_index(self, index: int):
        if index is None:
            return None

        val = self
        i = 0

        while i < index:
            val = val.next
            i += 1

        return val

    def from_list(self, values: list[list[int]]):
        val = self
        for i, tup in enumerate(values):
            if val is not None:
                val.val = tup[0]

            if i < len(values) - 1:
                val.next = Node(x=values[i + 1][0])
            val = val.next

        val = self
        i = 0

        while val:
            target_idx = values[i][1]
            val.random = self.get_index(target_idx)
            val = val.next
            i += 1


def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None
    new_head = Node(x=head.val)

    source_node: Node = head
    result_node = new_head

    node_map = {}

    while source_node:
        next_node = None

        if source_node.next:
            next_node = Node(x=source_node.next.val)

        result_node.next = next_node

        if source_node not in node_map:
            node_map[source_node] = result_node

        result_node = next_node

        source_node = source_node.next

    source_node: Node = head
    result_node: Node = new_head

    while source_node:
        result_node.random = (
            node_map[source_node.random] if source_node.random else None
        )
        source_node = source_node.next
        result_node = result_node.next

    return new_head


values = [[3, None], [7, 3], [4, 0], [5, 1]]

head = Node(x=0)

head.from_list(values=values)

node = head
while node:
    print(f"Current node: {node.val} ({node})")
    print(f"Next node: {node.next.val if node.next else node.next} ({node.next})")
    print(
        f"Rand node: {node.random.val if node.random else node.random} ({node.random})"
    )

    node = node.next


new_head = copyRandomList(head=head)

node = new_head

while node:
    print(f"Current node: {node.val} ({node})")
    print(f"Next node: {node.next.val if node.next else node.next} ({node.next})")
    print(
        f"Rand node: {node.random.val if node.random else node.random} ({node.random})"
    )

    node = node.next
