from typing import Optional
from linked_list.list_node import ListNode


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast, slow = head, head
    prev_node = None
    count = 0
    while count < n:
        fast = fast.next

    while fast:
        fast = fast.next
        prev_node = slow
        slow = slow.next

    if prev_node is None:
        head = head.next
    elif slow:
        prev_node.next = slow.next
    else:
        prev_node.next = slow
    return head


values = [1, 2, 3, 4]
n = 2
head = ListNode()
head.from_list(values)

result = removeNthFromEnd(head=head, n=n)
print(result)

node = result
i = 0
while node:
    print(f"Index: {i}")
    print(str(node.val) + "\n")
    i += 1
    node = node.next
