from typing import Optional
from linked_list.list_node import ListNode


def reverseListStack(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    stack = []
    node = head

    while node is not None:
        stack.append(node.val)
        node = node.next

    node = head

    while stack:
        if node is not None:
            node.val = stack.pop()
            node = node.next

    return head


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    prev_node = None
    cur_node = head

    while cur_node is not None:
        next_node = cur_node.next

        if prev_node is not None:
            cur_node.next = prev_node

        prev_node = cur_node
        cur_node = next_node

    head = prev_node
    return head


def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:

    if head is None:
        return None

    pass


source = [0, 1, 2, 3]

head = ListNode(0)
head.from_list(source)

result = reverseList(head=head)

print(result)
