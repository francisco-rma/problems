class Node:
    def __init__(self, key: int, val: int, next=None):
        self.key = key
        self.val = val
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_count = 0
        self.head: Node = None

    def display(self):
        keys = []
        values = []
        info = []
        node = self.head

        while node:
            keys.append(str(node.key))
            values.append(str(node.val))
            info.append(str(hex(id(node))))
            node = node.next

        l1 = "Key: " + " ---> ".join(keys)
        l2 = "Val: " + " ---> ".join(values)
        l3 = "Addr " + " ---> ".join(info)

        print(l1)
        print(l2)
        print(l3)
        print()

    def get(self, key: int) -> int:
        current_node = self.head
        previous_node: Node = None
        target_node: Node = None
        result = -1

        while current_node:
            if current_node.key == key:
                next_node: Node = current_node.next

                current_node.next = None

                target_node = current_node
                result = target_node.val

                if current_node is self.head:
                    self.head = next_node
                else:
                    previous_node.next = next_node

                if next_node:
                    previous_node = next_node
                    current_node = next_node.next
                else:
                    current_node = next_node

                continue

            previous_node = current_node
            current_node = current_node.next

        if target_node:
            target_node.next = None

        if previous_node:
            previous_node.next = target_node

        else:
            self.head = target_node

        return result

    def put(self, key: int, value: int) -> None:
        current_node = self.head
        previous_node: Node = None
        target_node: Node = None

        while current_node:
            if current_node.key == key:
                next_node: Node = current_node.next

                current_node.val = value
                current_node.next = None

                target_node = current_node

                if current_node is self.head:
                    self.head = next_node
                else:
                    previous_node.next = next_node

                if next_node:
                    previous_node = next_node
                    current_node = next_node.next
                else:
                    current_node = next_node

                continue

            previous_node = current_node
            current_node = current_node.next

        if not target_node:
            target_node = Node(key=key, val=value)
            self.current_count += 1

        target_node.next = None

        if not previous_node:
            self.head = target_node
        elif previous_node is not target_node:
            previous_node.next = target_node

        if self.current_count > self.capacity:
            self.head = self.head.next
            self.current_count -= 1


def test1():
    cache = LRUCache(2)
    cache.display()

    print(f"cache.put(1, 1) returned: {cache.put(1, 1)}")
    cache.display()

    print(f"cache.put(2, 2) returned: {cache.put(2, 2)}")
    cache.display()

    print(f"cache.get(1) returned: {cache.get(1)}")
    cache.display()

    print(f"cache.put(3, 3) returned: {cache.put(3, 3)}")
    cache.display()

    print(f"cache.get(2) returned: {cache.get(2)}")
    cache.display()

    print(f"cache.put(4, 4) returned: {cache.put(4, 4)}")
    cache.display()

    print(f"cache.get(1) returned: {cache.get(1)}")
    cache.display()

    print(f"cache.get(3) returned: {cache.get(3)}")
    cache.display()

    print(f"cache.get(4) returned: {cache.get(4)}")
    cache.display()


def test2():
    cache = LRUCache(2)
    cache.display()

    print(f"cache.put(1, 10) returned: {cache.put(1, 10)}")
    cache.display()

    print(f"cache.get(1) returned: {cache.get(1)}")
    cache.display()

    print(f"cache.put(2, 20) returned: {cache.put(2, 20)}")
    cache.display()

    print(f"cache.put(3, 30) returned: {cache.put(3, 30)}")
    cache.display()

    print(f"cache.get(2) returned: {cache.get(2)}")
    cache.display()

    print(f"cache.get(1) returned: {cache.get(1)}")
    cache.display()


def test3():
    cache = LRUCache(2)
    cache.display()

    print(f"cache.get(2) returned: {cache.get(2)}")
    cache.display()

    print(f"cache.put(2, 6) returned: {cache.put(2, 6)}")
    cache.display()

    print(f"cache.get(1) returned: {cache.get(1)}")
    cache.display()

    print(f"cache.put(1, 5) returned: {cache.put(1, 5)}")
    cache.display()

    print(f"cache.put(1, 2) returned: {cache.put(1, 2)}")
    cache.display()

    print(f"cache.get(1) returned: {cache.get(1)}")
    cache.display()

    print(f"cache.get(2) returned: {cache.get(2)}")
    cache.display()


test3()
