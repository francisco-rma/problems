def print_sub_diretories(paths: list[str]):
    class Tree:
        def __init__(self, value="", children=None):
            self.value = None
            self.children = []

            if value is not None:
                self.value = value
            if children is not None:
                self.children = children

        def add_child(self, child):
            if isinstance(child, Tree):
                self.children.append(child)
            else:
                self.children.append(Tree(child))

        def print_values(self, indent: int = -1):
            if not indent == 0:
                print(" " * indent + str(self.value))

            for child in self.children:
                child.print_values(indent + 1)

    root = Tree("root")

    for path in paths:
        node = root
        components = path.split("/")[1:]
        for comp in components:
            node_check = next((x for x in node.children if x.value == comp), None)
            if node_check is None:
                new_node = Tree(comp)
                node.children.append(new_node)
                node = new_node
            else:
                node = node_check

    root.print_values(indent=0)
    pass


paths = [
    "/foo/bar/bacon",
    "/x/uy/kz",
    "/abc/1",
    "/abc/18",
    "/abc/1/10",
    "/x/uy/kz/12",
]

print_sub_diretories(paths=paths)
