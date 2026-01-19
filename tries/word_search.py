from collections import deque
from string import ascii_lowercase

CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"


class WordDictionary:
    def __init__(self):
        self.values = [None] * len(ascii_lowercase)
        self.transitive: bool = True

    def __repr__(self):
        def display(node: WordDictionary, prefix="", is_left=True) -> str:
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

    def index_map(self, char):
        result = -1 if char == "." else ord(char) - ord("a")
        return result

    def addWord(self, word: str) -> None:
        node = self

        for char in word:
            idx = node.index_map(char)
            if node.values[idx] is None:
                node.values[idx] = WordDictionary()
            node = node.values[idx]

        assert node is not None
        node.transitive = False

    def search(self, word: str) -> bool:
        queue = deque(map(self.index_map, word))

        nodes = [self]
        while queue:
            if len(nodes) == 0:
                return False

            idx = queue.popleft()

            new_nodes = []
            for node in nodes:
                if idx == -1:
                    for idx, child in enumerate(node.values):
                        if child is not None:
                            new_nodes.append(child)
                elif node.values[idx] is not None:
                    new_nodes.append(node.values[idx])
                else:
                    continue
            nodes = new_nodes

        return len(nodes) > 0 and any(not node.transitive for node in nodes)


def basic_test1():
    wordDictionary: WordDictionary = WordDictionary()
    wordDictionary.addWord("day")
    wordDictionary.addWord("bay")
    wordDictionary.addWord("may")
    wordDictionary.addWord("gay")

    print(wordDictionary)

    key: str = "say"
    result = wordDictionary.search(key)
    print(f"key: {key} - result: {result}")
    assert result is False

    key = "gay"
    result = wordDictionary.search(key)
    print(f"key: {key} - result: {result}")
    assert result is True

    key = "day"
    result = wordDictionary.search(key)
    print(f"key: {key} - result: {result}")
    assert result is True

    key = ".ay"
    result = wordDictionary.search(key)
    print(f"key: {key} - result: {result}")
    assert result is True

    key = "b.."
    result = wordDictionary.search(key)
    print(f"key: {key} - result: {result}")
    assert result is True

    key = "..."
    result = wordDictionary.search(key)
    print(f"key: {key} - result: {result}")
    assert result is True


def basic_test2():
    wordDictionary: WordDictionary = WordDictionary()
    wordDictionary.addWord("dog")

    print(wordDictionary)

    key: str = "do.."
    result = wordDictionary.search(key)
    print(f"key: {key} - result: {result}")
    assert result is False


def basic_test3():
    wordDictionary: WordDictionary = WordDictionary()
    wordDictionary.addWord("one")
    wordDictionary.addWord("two")
    wordDictionary.addWord("three")

    print(wordDictionary)

    key: str = ".."
    result = wordDictionary.search(key)
    print(f"key: {key} - result: {result}")
    assert result is False


if __name__ == "__main__":
    basic_test1()
    basic_test2()
    basic_test3()
