from typing import Optional
from linked_list.list_node import ListNode


def reorder_list(head: Optional[ListNode]) -> None:
    def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        cur_node = head

        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        return prev_node

    def alternating_merge(head1: Optional[ListNode], head2: Optional[ListNode]):
        node = head1
        right = head2

        while node:
            next_node = node.next
            node.next = right
            if right:
                right = right.next
            if not next_node:
                break
            node.next.next = next_node
            node = node.next.next

        return

    count = 0
    node = head

    while node:
        count += 1
        node = node.next

    i = 1

    node = head
    while i < count // 2:
        node = node.next
        i += 1

    list2 = node.next
    node.next = None

    list2 = reverse(list2)

    alternating_merge(head, list2)
    return


my_list1 = [2, 4, 6, 8, 10]
my_list2 = [2, 4, 6, 8]


head = ListNode(0)
head.from_list(my_list2)
reorder_list(head)

node = head
while node:
    print(node.val)
    node = node.next
