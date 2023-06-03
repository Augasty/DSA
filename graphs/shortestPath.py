import collections

def shortest(graph,start,end):
    queue = collections.deque([[start,0]]) #node and dist
    visited = set([start])
    while len(queue) > 0:
        node , dist = queue.pop()

        
        if node == end:
            return dist

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.appendleft([nei,dist + 1])

    return -1








edges = [[1,2],[2,1],[2,3],[3,2],[4,3],[3,4],[4,5],[5,4],[5,1],[1,5]]

def buildGraph(edges):
    graph = {}
    for edge in edges:
        a , b = edge  
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

graph = buildGraph(edges)

print(shortest(graph,1,4))