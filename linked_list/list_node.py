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
