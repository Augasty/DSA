graph = {
    1:[3,4],
    2:[5,3],
    3:[4],
    4:[],
    5:[1,3]
}

def topological(graph):
    incomings = {node: 0 for node in graph}
    for node in graph:
        for nei in graph[node]:
            incomings[nei] += 1


    noIncomings = []
    for node in incomings:
        if incomings[node] == 0:
            noIncomings.append(node)

    topoOrder = []
    while noIncomings:
        node = noIncomings.pop()
        topoOrder.append(node)

        for nei in graph[node]:
            incomings[nei] -= 1
            if incomings[nei] == 0:
                noIncomings.append(nei)
    if len(topoOrder) == len(graph):
        return topoOrder
print(topological(graph))