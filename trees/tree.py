class Tree(object):

    def __init__(self, value="", children=None) -> None:
        self.children = []
        self.value = None
        if value is not None:
            self.value = value
        if children is not None:
            self.children = children
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


tree = Tree("root")
tree.add_child("first child 1")
tree.children[0].add_child(Tree("second child 1"))
tree.children[0].add_child(Tree("second child 2"))
tree.children[0].add_child(Tree("second child 3"))
tree.children[0].children[0].add_child(Tree("third child 1"))
test = tree.search("second child 2")

print(test)
