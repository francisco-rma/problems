from __future__ import annotations


class ListNode:
    def __init__(self, val: int, next: ListNode = None):
        self.val = val
        self.next = next

    def from_list(values: list[int]):
        head = ListNode(0)
        node = head
        for idx, val in enumerate(values):
            node.val = val

            if idx < len(values) - 1:
                node.next = ListNode(0)

            node = node.next
        return head

    def findDuplicate(self) -> int:
        counts = {}

        node = self

        while node is not None:
            if node.val in counts.keys():
                return node.val

            counts[node.val] = 1

            node = node.next

        return False

    def floydfindDuplicate(nums: list[int]) -> int:
        fast, slow = nums[0], nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        new_slow = nums[0]

        while new_slow != slow:
            new_slow = nums[new_slow]
            slow = nums[slow]

        return new_slow


nums = [1, 2, 3, 4, 4]
ll: ListNode = ListNode.from_list(nums)

result = ListNode.floydfindDuplicate(nums)
print(f"The repeating number is: {result}")
