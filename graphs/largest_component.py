def largestComponent(graph):
    maxm = 0
    visited = set()

    for node in graph.keys():
        if node not in visited:
            visited = set()  #if the node is not visited, then it means that it is a new and disconnected component of the graph
            maxm = max(maxm,dfs(graph, node ,visited))
    return maxm


def dfs(graph,src,visited):
    if src in visited:
        return 
    visited.add(src)
    for n in graph[src]:
        dfs(graph,n,visited)
    return len(visited)

graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

print(largestComponent(graph))