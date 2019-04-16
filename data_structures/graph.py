from math import inf

from data_structures.heap import MinHeap, Node
from data_structures.queue import Queue


class Graph:
    def __init__(self, directed=True):
        self.adjacency_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight=1):
        if from_vertex not in self.adjacency_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adjacency_list:
            self.add_vertex(to_vertex)

        self.adjacency_list[from_vertex].append((to_vertex, weight))
        if not self.directed:
            self.adjacency_list[to_vertex].append((from_vertex, weight))

    def _initialize_visited_set(self):
        return {vertex: False for vertex in self.adjacency_list}

    # Return a path between source_vertex and target_vertex if existent
    def depth_first_search(self, source_vertex, target_vertex):
        visited = self._initialize_visited_set()
        path = []
        self._dfs_helper(source_vertex, target_vertex, visited, path)
        return path

    def _dfs_helper(self, source_vertex, target_vertex, visited, path):
        visited[source_vertex] = True
        path.append(source_vertex)
        if source_vertex == target_vertex:
            return True
        for neighbor, _ in self.adjacency_list[source_vertex]:
            if not visited[neighbor]:
                if self._dfs_helper(neighbor, target_vertex, visited, path):
                    return True
        path.pop()

    # Return the shortest path between source and target if existent in an unweighted graph
    def breadth_first_search(self, source_vertex, target_vertex):
        visited = self._initialize_visited_set()
        visited[source_vertex] = True

        vertices_to_visit = Queue()
        vertices_to_visit.enqueue(source_vertex)

        history = {source_vertex: None}
        path = []
        while not vertices_to_visit.is_empty():
            current_vertex = vertices_to_visit.dequeue()
            if current_vertex == target_vertex:
                break
            for neighbor, _ in self.adjacency_list[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    history[neighbor] = current_vertex
                    vertices_to_visit.enqueue(neighbor)

        if target_vertex in history:
            while target_vertex is not None:
                path.insert(0, target_vertex)
                target_vertex = history[target_vertex]
        return path

    # Return the shortest path from a vertex to every other reachable vertex in a weighted graph
    def dijkstra_shortest_path(self, source_vertex):
        visited = {}
        distances = MinHeap()

        for vertex in self.adjacency_list:
            distances.add(Node(vertex, inf))
        distances.update(source_vertex, 0, None)
        
        while not distances.is_empty():
            current_vertex = distances.poll()
            for neighbor, weight in self.adjacency_list[current_vertex.key]:
                if neighbor not in visited and neighbor is not current_vertex.key:
                    distance = current_vertex.distance + weight
                    if distance < distances.get(neighbor).distance:
                        distances.update(neighbor, distance, current_vertex)

            visited[current_vertex.key] = current_vertex
        return visited


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge("a", "b")
    graph.add_edge("a", "c")
    graph.add_edge("b", "c")
    graph.add_edge("c", "d")
    graph.add_edge("d", "d")
    graph.add_edge("c", "a")
    graph.add_edge("b", "e")

    #      a   b   c   d   e
    #     ___ ___ ___ ___ ___
    # a  | 0   1   1   0   0
    # b  | 0   0   1   0   1
    # c  | 1   0   0   1   0
    # d  | 0   0   0   1   0
    # e  | 0   0   0   0   0

    print("###########################\n# Depth First Search\n############################")
    print(graph.depth_first_search("a", "d"))

    print("\n###########################\n# Breadth First Search\n###########################")
    print(graph.breadth_first_search("a", "d"))

    print("\n###########################\n# Dijkstra's Shortest Path\n###########################")
    graph = Graph()
    graph.add_edge("a", "b", 10)
    graph.add_edge("a", "c", 5)
    graph.add_edge("b", "c", 9)
    graph.add_edge("c", "d", 13)
    graph.add_edge("d", "d", 0)
    graph.add_edge("c", "a", 3)
    graph.add_edge("b", "e", 4)

    #      a   b   c   d   e
    #     ___ ___ ___ ___ ___
    # a  | 0  10   5   -   -
    # b  | -   0   9   -   4
    # c  | 3   -   0   13  0
    # d  | -   -   -   0   -
    # e  | -   -   -   -   0

    def get_path_to(paths, to_vertex):
        node = paths[to_vertex]
        path = []
        while node:
            path.insert(0, (node.key, node.distance))
            node = node.previous
        return path


    print("\n### FROM B")
    shortest_paths = graph.dijkstra_shortest_path("b")
    print(get_path_to(shortest_paths, "a"))
    print(get_path_to(shortest_paths, "b"))
    print(get_path_to(shortest_paths, "c"))
    print(get_path_to(shortest_paths, "d"))
    print(get_path_to(shortest_paths, "e"))

    print("\n### Added (b, a)")
    graph.add_edge("b", "a", 2)

    print("\n### FROM B")
    shortest_paths = graph.dijkstra_shortest_path("b")
    print(get_path_to(shortest_paths, "a"))
    print(get_path_to(shortest_paths, "b"))
    print(get_path_to(shortest_paths, "c"))
    print(get_path_to(shortest_paths, "d"))
    print(get_path_to(shortest_paths, "e"))

    print("\n### FROM E")
    shortest_paths = graph.dijkstra_shortest_path("e")
    print(get_path_to(shortest_paths, "a"))
    print(get_path_to(shortest_paths, "b"))
    print(get_path_to(shortest_paths, "c"))
    print(get_path_to(shortest_paths, "d"))
    print(get_path_to(shortest_paths, "e"))

    print("\n### FROM D")
    shortest_paths = graph.dijkstra_shortest_path("d")
    print(get_path_to(shortest_paths, "a"))
    print(get_path_to(shortest_paths, "b"))
    print(get_path_to(shortest_paths, "c"))
    print(get_path_to(shortest_paths, "d"))
    print(get_path_to(shortest_paths, "e"))

    graph = Graph(False)
    for vertex in range(1, 6):
        graph.add_vertex(vertex)
    graph.add_edge(1, 2, 10)
    graph.add_edge(1, 3, 6)
    graph.add_edge(2, 4, 8)
    s = 2
    shortest_paths = graph.dijkstra_shortest_path(s)
    print([value.distance if value.distance != inf else -1 for key, value in sorted(shortest_paths.items()) if key != s])

