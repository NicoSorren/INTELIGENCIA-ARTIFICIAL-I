def DFS_path(graph, start, end, path=None):
    if path is None:
        path = []
        
    path.append(start)
    
    if start == end:
        return path

    for v in graph.get_neighbours(start):
        if v not in path:
            new_path = DFS_path(graph, v, end, path)
            if new_path is not None:
                return new_path
    return None
