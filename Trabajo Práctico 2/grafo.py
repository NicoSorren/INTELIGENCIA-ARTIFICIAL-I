class Directed_Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            return "vertex already in graph"
        self.graph_dict[vertex] = []

    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        cost = edge.get_cost()
        if v1 not in self.graph_dict or v2 not in self.graph_dict:
            raise ValueError(f"One or more vertices not in graph: {v1.get_name()}, {v2.get_name()}")
        self.graph_dict[v1].append((v2, cost))

    def get_neighbours(self, vertex):
        return self.graph_dict[vertex]

    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f'Vertex {vertex_name} does not exist')


class Edge:
    def __init__(self, v1, v2, cost=1):
        self.v1 = v1
        self.v2 = v2
        self.cost = cost

    def get_v1(self):
        return self.v1

    def get_v2(self):
        return self.v2

    def get_cost(self):
        return self.cost


class Vertex:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


def manhattan_distance(start, goal):
    coordinates = {
        'I': (1, 2), 'G': (0, 2), 'W': (1, 3), 'K': (1, 4),
        'P': (2, 0), 'Q': (2, 1), 'R': (2, 2), 'T': (2, 3),
        'M': (1, 5), 'N': (1, 6), 'F': (2, 6)
    }
    x1, y1 = coordinates[start.get_name()]
    x2, y2 = coordinates[goal.get_name()]
    return abs(x1 - x2) + abs(y1 - y2)
