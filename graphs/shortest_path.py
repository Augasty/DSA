# shortest path using DFS ..... not the normal way

def shortest(graph,start,end):
    length = 0

    return bfs(graph,start,end,length,set())

def bfs(graph,start,end,length,visited):
    queue = [start]
    
    while len(queue) > 0:
        current = queue.pop()
        while current in visited:
            current = queue.pop()

        visited.add(current)
        if current == end:
            return length
        else:
            print(current)
            length += 1

        for nei in graph[current]:
            queue.append(nei)


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