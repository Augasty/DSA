#iterative dfs
"""
we push the first item in the stack ("a" here). Then we enter the while loop. 
We pop and print the current element and print it(a here). Now we add all the neighbours of
our current element ( ["b","c"] here) TO THE RIGHT of the stack.

Now the current element is "c" here. And stack looks like     stack =  ["b","c"]
We pop and print "c" and add all it's neighbours ("e" here). Now the stack looks like    stack =  ["b","e"]
we pop and print "e", and add all it's neighbours... no neighbours are there. Now, stack =  ["b"]

Now we pop and print "b", and add it's neighbours ("d").  stack = ["d"]
Now we pop and print "d", and add it's neighbours ("f").  stack = ["f"]
Now we pop and print "f", and add it's neighbours (it has none).  stack = []

at the end of this while loop, len(stack) == 0, and the loop breaks. So we come out of it and finish execution.
"""
def printDfs(graph,source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        
        # opt 1. concating the stack with the neighbours
        # stack = stack + graph[current]

        # opt 2. going through every neighbour of the current element and adding them one by one
        for neighbour in graph[current]:
            stack.append(neighbour)

    


graph = { "a" : ["b","c"],
          "b" : ["d"],
          "c" : ["e"],
          "d" : ["f"],
          "e" : [],
          "f" : []
        }


printDfs(graph,"a")

