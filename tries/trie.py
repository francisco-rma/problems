from __future__ import annotations

from collections import deque
from string import ascii_lowercase
from typing import Optional

CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"


class PrefixTree:
    def __init__(self):
        self.values: list[Optional[PrefixTree]] = [None] * len(ascii_lowercase)
        self.transitive = True

    @staticmethod
    def display_v1(node: PrefixTree, prefix="", is_left=True) -> str: ...

    def __repr__(self):
        def display(node: PrefixTree, prefix="", is_left=True) -> str:
            result = ""
            for i in range(len(ascii_lowercase) - 1, -1, -1):
                child = node.values[i]
                if child is not None:
                    new_prefix = prefix + ("│   " if is_left else "    ")
                    result += display(child, new_prefix, False)
                    result += prefix
                    if prefix:
                        result += "└── " if is_left else "┌── "
                    char = ascii_lowercase[i]
                    if child.transitive:
                        result += f"{CYAN}{char}{RESET}\n"
                    else:
                        result += f"{GREEN}{char}{RESET}\n"
            return result

        return display(self).rstrip()

    def index_map(self, char: str) -> int:
        return ord(char) - ord("a")

    def insert(self, word: str) -> None:
        queue = deque(map(self.index_map, word))
        node = self
        while queue:
            char_idx = queue.popleft()
            assert node is not None
            if node.values[char_idx] is None:
                node.values[char_idx] = PrefixTree()
            node = node.values[char_idx]
        assert node is not None
        node.transitive = False

    def search(self, word: str) -> bool:
        queue = deque(map(self.index_map, word))
        node = self
        while queue:
            char_idx = queue.popleft()
            if node.values[char_idx] is None:
                return False
            node = node.values[char_idx]
        return not node.transitive

    def startsWith(self, prefix: str) -> bool:
        queue = deque(map(self.index_map, prefix))
        node = self
        while queue:
            char_idx = queue.popleft()
            if node.values[char_idx] is None:
                return False
            node = node.values[char_idx]
        return True


def basic_test():
    trie = PrefixTree()
    trie.insert("dog")
    trie.insert("god")
    trie.insert("goodbye")

    assert trie.search("dog") is True
    assert trie.search("god") is True
    assert trie.search("goodbye") is True
    assert trie.search("good") is False

    assert trie.startsWith("go") is True
    assert trie.startsWith("god") is True
    assert trie.startsWith("gode") is False
    assert trie.startsWith("do") is True
    assert trie.startsWith("bad") is False

    trie.insert("hello")
    trie.insert("hey")
    trie.insert("goodbye")
    trie.insert("heat")

    assert trie.search("helicopter") is False
    assert trie.search("goodmorning") is False
    assert trie.search("zebra") is False

    assert trie.startsWith("he") is True
    assert trie.startsWith("go") is True
    assert trie.startsWith("ze") is False

    print("✓ Passed basic tests")
    print(trie)


if __name__ == "__main__":
    basic_test()
