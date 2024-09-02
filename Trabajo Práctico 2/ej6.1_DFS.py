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
        if v1 not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} not in graph')
        if v2 not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} not in graph')
        self.graph_dict[v1].append(v2)
    
    def is_vertex_in(self,vertex):
        return vertex in self.graph_dict # chequea que nodo este en diccionario
    
    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f'Vertex {vertex_name} does not exist')
        
    def get_neighbours(self, vertex): ## seria como nodos hijos
        return self.graph_dict[vertex]
    
    def __str__(self):
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() + '---->' + v2.get_name() + '\n'     ## imprime cada llave con elemetnos dentro de la misma
        return all_edges


    

class Edge:     # aristas que une un nodo con otro
    def __init__(self, v1, v2):
        self.v1 = v1       # Nodo de inicio
        self.v2 = v2       # Nodo de destino
    def get_v1(self):
        return self.v1
    def get_v2(self):
        return self.v2
    def __str__(self):
        return  self.v1.get_name() + '---->' + self.v2.get_name()

class Vertex:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name
    
def build_graph(graph):
    g = graph()
    for v in ('I','G','Q','W','P','O','R','T', 'K', 'M','C', 'N', 'F', 'A','E', 'B', 'D'):
        g.add_vertex(Vertex(v))
    g.add_edge(Edge(g.get_vertex('I'), g.get_vertex('G')))
    g.add_edge(Edge(g.get_vertex('I'), g.get_vertex('Q')))
    g.add_edge(Edge(g.get_vertex('I'), g.get_vertex('W')))
    g.add_edge(Edge(g.get_vertex('G'), g.get_vertex('P')))
    g.add_edge(Edge(g.get_vertex('P'), g.get_vertex('Q')))
    g.add_edge(Edge(g.get_vertex('Q'), g.get_vertex('R')))
    g.add_edge(Edge(g.get_vertex('R'), g.get_vertex('T')))
    g.add_edge(Edge(g.get_vertex('W'), g.get_vertex('K')))
    g.add_edge(Edge(g.get_vertex('K'), g.get_vertex('M')))
    g.add_edge(Edge(g.get_vertex('K'), g.get_vertex('C')))
    g.add_edge(Edge(g.get_vertex('M'), g.get_vertex('N')))
    g.add_edge(Edge(g.get_vertex('M'), g.get_vertex('F')))
    g.add_edge(Edge(g.get_vertex('N'), g.get_vertex('E')))
    g.add_edge(Edge(g.get_vertex('C'), g.get_vertex('A')))
    g.add_edge(Edge(g.get_vertex('A'), g.get_vertex('B')))
    g.add_edge(Edge(g.get_vertex('B'), g.get_vertex('D')))

    return g

G1 = build_graph(Directed_Graph)

print(G1)


def DFS_path(graph, start, end, path):
    path.append(start)
    
    if start == end:
        return path

    for v in graph.get_neighbours(start):
        if v not in path:                       # evita duplicidades
            new_path = DFS_path(graph, v, end, path)
            if new_path is not None:
                return new_path
            

path = DFS_path(G1, G1.get_vertex('I'), G1.get_vertex('F'), [])         # lista que contiene objetos tipo nodo

for v in path:
    print(f'"{v.get_name()}"')