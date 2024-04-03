class Node(object):

    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = None
        self.left = None
        self.right = None
        if value is not None:
            self.value = value
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        pass

    def search(self, target):
        print(f"Value: {self.value}")
        children = [child.value for child in self.children]
        if self.value == target:
            return self
        elif self.children is None or len(self.children) <= 0:
            return None
        else:
            for child in self.children:
                test = child.search(target)
                if test is None:
                    continue
                else:
                    return test

    def add_child(self, child):
        if isinstance(child, Tree):
            self.children.append(child)
        else:
            self.children.append(Tree(child))
