from math import inf

from data_structures.graph import Graph


def shortest_reach(n, edges, s):
    graph = Graph(False)
    for vertex in range(1, n + 1):
        graph.add_vertex(vertex)
    for begin, end, weight in edges:
        graph.add_edge(begin, end, weight)
    shortest_paths = graph.dijkstra_shortest_path(s)
    return [value.distance if value.distance != inf else -1 for key, value in sorted(shortest_paths.items()) if key != s]


if __name__ == '__main__':
    with open('dijkstra_test_6', 'r') as test:
        t = test.readline()
        for t_itr in range(int(t)):
            nm = test.readline().split()
            n = int(nm[0])
            m = int(nm[1])
            edges = []
            for _ in range(m):
                edges.append(list(map(int, test.readline().rstrip().split())))
            s = int(test.readline())
            result = shortest_reach(n, edges, s)
            print(result)
            print("\n")
