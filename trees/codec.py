# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # Pretty print the tree with connections
        def display(node, prefix="", is_left=True) -> str:
            if not node:
                return ""
            result = ""
            if node.right:
                new_prefix = prefix + ("│   " if is_left else "    ")
                result += display(node.right, new_prefix, False)
            result += prefix
            if prefix:
                result += "└── " if is_left else "┌── "
            result += f"{node.val}\n"
            if node.left:
                new_prefix = prefix + ("    " if is_left else "│   ")
                result += display(node.left, new_prefix, True)
            return result

        return display(self).rstrip()

    def insert(self, key): ...


class Codec:
    def __init__(self, delimiter=",", sentinel="N"):
        self.delimiter = delimiter
        self.sentinel = sentinel

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                result.append(self.sentinel)
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.delimiter.join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.idx = 0
        source = data.split(self.delimiter)
        print(source)

        def dfs():
            if source[self.idx] == self.sentinel:
                self.idx += 1
                return None

            node = TreeNode(int(source[self.idx]))
            self.idx += 1

            node.left = dfs()
            node.right = dfs()

            return node

        root = dfs()
        return root


if __name__ == "__main__":
    codec = Codec()
    tree = codec.deserialize("1,2,3,N,N,4,5")
    print("tree:\n", tree)
    serialized = codec.serialize(tree)
    print("serialized:", serialized)
