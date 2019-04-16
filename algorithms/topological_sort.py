from typing import Any, Set

from data_structures.graph import Graph
from data_structures.stack import Stack


def topological_sort(graph: Graph) -> None:
    visited = set()
    stack = Stack()
    for vertex in graph.adjacency_list:
        if vertex not in visited:
            _topological_sort(graph, vertex, visited, stack)
    print(stack)


def _topological_sort(graph: Graph, vertex: Any, visited: Set, stack: Stack) -> None:
    visited.add(vertex)

    for neighbor in graph.adjacency_list[vertex]:
        if neighbor[0] not in visited:
            _topological_sort(graph, neighbor[0], visited, stack)

    stack.push(vertex)


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(4, 1)
    graph.add_edge(4, 0)

    topological_sort(graph)
