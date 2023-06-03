def hasPath(graph,source,target):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        if current == target:
            return True
        for neighbour in graph[current]:
            stack.append(neighbour)


    return False


graph = { "a" : ["b","c"],
          "b" : ["d"],
          "c" : ["e"],
          "d" : ["f"],
          "e" : [],
          "f" : []
        }

if hasPath(graph,"c","f"):
    print("yes")
else:
    print("no")