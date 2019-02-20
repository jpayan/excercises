# Considering a list of positive integers where each item represents the maximum steps you can take
# return the minimum amount of steps to get from index 0 to index size - 1

from random import randint
from typing import Dict, List

from data_structures.queue import Queue


def get_least_amount_of_steps(steps: List[int]) -> List[int]:
    return breadth_first_search(steps, 0, len(steps) - 1)


def breadth_first_search(graph: List[int], source_vertex: int, target_vertex: int) -> List[int]:
    vertices_to_visit = Queue()
    vertices_to_visit.enqueue(source_vertex)

    # distances = {source_vertex: 0}  # Use this to get number of steps
    history = {source_vertex: None}  # Use this to get path

    while not vertices_to_visit.is_empty():
        current_vertex = vertices_to_visit.dequeue()
        for neighbor in range(1, graph[current_vertex] + 1):
            neighbor_index = current_vertex + neighbor
            if neighbor_index < len(graph):
                # if neighbor_index not in distances:
                if neighbor_index not in history:
                    # distances[neighbor_index] = distances[current_vertex] + 1
                    history[neighbor_index] = current_vertex
                    if neighbor_index == target_vertex:
                        # return distances[target_vertex]
                        return get_path(history, target_vertex)
                    vertices_to_visit.enqueue(neighbor_index)


def get_path(history: Dict[int, int], target_vertex: int):
    path = []
    if target_vertex in history:
        while target_vertex is not None:
            path.insert(0, target_vertex)
            target_vertex = history[target_vertex]

    return path


if __name__ == '__main__':
    max_steps = 100
    max_nodes = 1000
    steps = [randint(1, max_steps) for i in range(max_nodes)]
    print(get_least_amount_of_steps(steps))
