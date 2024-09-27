from typing import Optional
from linked_list.list_node import ListNode


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:

    if list1 is None and list2 is None:
        return None
    elif list1 is None:
        return list2
    elif list2 is None:
        return list1

    new_head = None
    left, right = list1, list2

    if left.val <= right.val:
        new_head = left
        left = left.next
    else:
        new_head = right
        right = right.next

    node = new_head

    while left and right:
        if left.val <= right.val:
            node.next = left
            left = left.next
        else:
            node.next = right
            right = right.next
        node = node.next

    if left:
        node.next = left

    if right:
        node.next = right

    return new_head


head1 = ListNode(0)
head2 = ListNode(0)

list1 = [-9, 3]
list2 = [5, 7]

head1.from_list(list1)
head2.from_list(list2)

result = mergeTwoLists(list1=head1, list2=head2)

print(f"Result: {result} --> Value: {result.val}")
