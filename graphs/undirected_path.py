edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]  #bidirectional

def buildGraph(edges):
    graph = {}

    # iterating through edges
    for edge in edges:
        a , b = edge  #destructuring the two values in every edge

        # if the node is not present, a node is created with empty adjecency lists
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        # neighbours are added
        graph[a].append(b)
        graph[b].append(a)

    return graph

# print(buildGraph(edges))


def hasPath(graph, src, dst, visited):
    if src in visited:
        return False
    if src == dst:
        return True
    visited.add(src)
    for i in graph[src]:
        if hasPath(graph,i,dst,visited) == True:
            return True

        

    return False


def undirected(edges,  src, dst):
    graph = buildGraph(edges)
    return hasPath(graph,  src, dst, set())


print(undirected(edges,0,1))