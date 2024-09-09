from grafo import Directed_Graph, Edge, Vertex
from dfs import DFS_path

def build_graph():
    g = Directed_Graph()
    for v in ('I', 'G', 'Q', 'W', 'P', 'O', 'R', 'T', 'K', 'M', 'C', 'N', 'F', 'A', 'E', 'B', 'D'):
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

if __name__ == "__main__":
    G1 = build_graph()
    print(G1)

    path = DFS_path(G1, G1.get_vertex('I'), G1.get_vertex('F'))
    
    if path:
        for v in path:
            print(f'"{v.get_name()}"')
    else:
        print("No path found.")
