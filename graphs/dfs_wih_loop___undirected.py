graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

def dfs(graph,src,visited):
    if src in visited:
        return
    
    print(src)
    
    visited.add(src)
    for n in graph[src]:
        dfs(graph,n,visited)
    return

print(dfs(graph,8,set()))
