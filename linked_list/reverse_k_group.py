from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def from_list(self, values: list[int]):
        val = self
        for i, value in enumerate(values):
            if val is not None:
                val.val = value

            if i < len(values) - 1:
                val.next = ListNode()
            val = val.next


def reverseKGroup(head: Optional[ListNode], k: int) -> tuple[ListNode, ListNode]:
    def reverse(
        root: ListNode, limit: ListNode, previous_root: Optional[ListNode] = None
    ):
        if root is None or limit is None:
            raise ValueError("Unallowed parameters")

        if previous_root is not None:
            previous_root.next = limit

        if limit is root:
            return (limit, root)

        node = root
        previous = None

        while node is not limit:
            temp = node.next
            node.next = limit.next if previous is None else previous
            previous = node
            node = temp
        node.next = previous
        return (limit, root)

    batch_count = 0

    count = 1
    node = head
    root = head
    previous_root = None

    while node is not None:
        if count == k:
            new_root, node = reverse(root=root, limit=node, previous_root=previous_root)
            count = 0

            if batch_count == 0:
                head = new_root
            batch_count += 1
            previous_root = node
            root = node.next

        node = node.next
        count += 1

    return head


test_values = [1, 2, 3, 4, 5]

head: ListNode = ListNode()
head.from_list(test_values)

node = reverseKGroup(head=head, k=1)
print(head)
idx = 0
while node is not None:
    print(f"Index: {idx} ----  value: {node.val}")
    node = node.next
    idx += 1
