import numpy as np
import pydot
from graphs.adjacency_matrix import adj_matrix


def dot_buffer(source: list[tuple[int, int]], directed=True):
    dot_string = ""
    if directed:
        dot_string += "digraph G {\n"
        edge_op = "->"
    else:
        dot_string += "graph G {\n"
        edge_op = "--"

    connections: dict[int, list[int]] = {}
    for a, b in source:
        if a not in connections:
            connections[a] = []
        connections[a].append(b)

    labels = list(connections.keys())

    for i in range(len(labels)):
        for j in range(len(labels)):
            if labels[j] in connections[labels[i]]:
                dot_string += f'  "{labels[i]}" {edge_op} "{labels[j]}";\n'
    dot_string += "}\n"

    return dot_string


def display(source: list[tuple[int, int]]):
    print("source:")
    print(source, "\n")

    adj_matrix(source)


def pydot_graph(source: list[tuple[int, int]]):
    graph = pydot.Dot("graph")

    for a, b in source:
        graph.add_edge(pydot.Edge(str(a), str(b)))

    graph.write("tuple_graph.png", format="png")
    with open("tuple_graph.svg", "wb") as f:
        buffer = graph.create_svg(prog="dot")
        f.write(buffer)


def pydot_matrix_to_graph(source: list[list[int]]):
    assert len(source) == len(source[0])
    graph = pydot.Dot("graph")
    population = range(len(source))
    for i in population:
        for j in population:
            if source[i][j] > 0:
                graph.add_edge(pydot.Edge(str(i), str(j)))

    graph.write("matrix_graph.png", format="png")
    with open("matrix_graph.svg", "wb") as f:
        buffer = graph.create_svg(prog="dot")
        f.write(buffer)


def draw_adjacency_matrix(adjacency_matrix: np.ndarray, node_order=None, partitions=[], colors=[]):
    """
    - G is a netorkx graph
    - node_order (optional) is a list of nodes, where each node in G
          appears exactly once
    - partitions is a list of node lists, where each node in G appears
          in exactly one node list
    - colors is a list of strings indicating what color each
          partition should be
    If partitions is specified, the same number of colors needs to be
    specified.
    """
    print(adjacency_matrix)


def pydot_cluster(source: list[tuple[int, int]]):
    graph = pydot.Dot("graph", graph_type="digraph")

    clusters: dict[int, pydot.Cluster] = {}
    for a, b in source:
        if a not in clusters:
            clusters[a] = pydot.Cluster(str(a), label=str(a))
        clusters[a].add_node(pydot.Node(str(b)))

    for cluster in clusters.values():
        graph.add_subgraph(cluster)

    graph.write("cluster_graph.png", format="png")
    with open("cluster_graph.svg", "wb") as f:
        buffer = graph.create_svg(prog="dot")
        f.write(buffer)


def generate():
    # 6 nodes, 0 is source, 5 is sink
    matrix = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            if i != j and np.random.rand() > 0.5:
                matrix[i, j] = np.random.randint(1, 10)
    # No incoming edges to source
    matrix[:, 0] = 0
    # No outgoing edges from sink
    matrix[5, :] = 0
    return matrix


def plot(matrix):
    assert len(matrix) == len(matrix[0])
    graph = pydot.Dot("max_flow", graph_type="digraph")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and matrix[i, j] > 0:
                graph.add_edge(pydot.Edge(str(i), str(j), label=str(matrix[i, j])))
    source_node = graph.get_node(str(0))[0]
    source_node.set_style("filled")
    source_node.set_fillcolor("red")
    sink_node = graph.get_node(str(5))[0]
    sink_node.set_style("filled")
    sink_node.set_fillcolor("green")
    graph.write("network_flow.png", format="png")
    with open("network_flow.svg", "wb") as f:
        buffer = graph.create_svg(prog="dot")
        f.write(buffer)


if __name__ == "__main__":
    matrix = generate()
    print("Creating network flow graph...")
    print(matrix)
    plot(matrix)
