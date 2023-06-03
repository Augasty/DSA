def checkComponents(graph):
    visited = set()
    count = 0
    for src in graph.keys():
        if src not in visited:
            dfs(graph,src,visited)
            count += 1
    return count

def dfs(graph,src,visited):
    if src in visited:  #to avoid going back to the previous node and creating an infinite loop
        return
    visited.add(src)
    for neighbour in graph[src]:
        dfs(graph,neighbour,visited)


graph = {
    3: [],
    4: [6],
    6: [4,5,7,8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}
# graph = { "a" : ["b","c"],
#           "b" : ["d"],
#           "c" : ["e"],
#           "d" : ["f"],
#           "e" : [],
#           "f" : []
#         }

print(checkComponents(graph))