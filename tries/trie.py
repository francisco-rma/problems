from collections import deque


class Trie:
    def __init__(self, val: int = 0):
        self.val: int = val
        self.children: list[Trie] = [None] * 128

    # TODO FIX
    def __repr__(self):
        if self is None:
            return

        queue = deque([self])
        val = ""
        level = 1

        while queue:
            node = queue.pop()
            test = list(filter(bool, node.children))
            for item in test:
                val += f"\nLevel {level} : {chr(item.val)}\n"
                queue.appendleft(item)

            level += 1
        return val

    def insert(self, key: str):
        node = self
        queue = deque(map(ord, key))
        level = 1
        while queue:
            idx = queue.popleft()
            if node.children[idx] is None:
                node.children[idx] = Trie(idx)
            node = node.children[idx]
            level += 1

    def search(self, key: str) -> bool:
        queue = deque(map(ord, key))
        node = self
        level = 1
        while queue:
            idx = queue.popleft()
            if node.children[idx] is None:
                print(f"Found {key[:level]}/{key}")
                return False

            node = node.children[idx]
            level += 1

        # print(f"Found {key[:level]}/{key}")
        return True
