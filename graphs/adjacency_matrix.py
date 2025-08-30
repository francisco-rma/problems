import numpy as np


def adj_matrix(source: list[tuple[int, int]]):
    connections: dict[int, list[int]] = {}
    for a, b in source:
        if a not in connections:
            connections[a] = []
        connections[a].append(b)
    print(connections)
    labels = list(connections.keys())

    matrix = np.zeros((len(labels), len(labels)))

    for i in range(len(labels)):
        for j in range(len(labels)):
            if labels[j] in connections[labels[i]]:
                matrix[i, j] = 1

    print(matrix)


source = [(1, 3), (2, 4), (3, 4), (4, 5)]
print("source:")
print(source, "\n")

adj_matrix(source)
