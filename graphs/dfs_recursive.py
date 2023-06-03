#recursive dfs

def printDfs(graph,source):
    print(source)

# the neighbours are the source when the function is called again
# when there is no neighbour, the for loop doesn't execute itself, so it acts as a deffault edge case
    for neighbour in graph[source]:
        printDfs(graph,neighbour)
    


graph = { "a" : ["b","c"],
          "b" : ["d"],
          "c" : ["e"],
          "d" : ["f"],
          "e" : [],
          "f" : []
        }


printDfs(graph,"a")

