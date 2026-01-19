import numpy as np
import pydot


def adj_matrix(source: list[tuple[int, int]]):
    individuals = set()
    for a, b in source:
        individuals.add(a)
        individuals.add(b)

    connections: dict[int, list[int]] = {}
    for a, b in source:
        if a not in connections:
            connections[a] = []
        if b not in connections:
            connections[b] = []
        connections[a].append(b)

    labels = sorted(list(individuals))
    population = range(len(labels))

    matrix = np.zeros((len(labels), len(labels)))

    for i in population:
        for j in population:
            if labels[j] in connections[labels[i]]:
                matrix[i, j] += 1

    return matrix
