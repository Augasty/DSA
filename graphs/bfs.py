import collections


"""
we push the first item in the deque ("a" here). Then we enter the while loop. 
We pop and print the current element and print it("a" here). Now we add all the neighbours of
our current element ( ["b","c"] here) TO THE LEFT of the stack, one by one. So, now the stack = ["c","b"]

Now the current element is "b" here. And stack looks like     stack = ["c","b"]
We pop and print "b" and add all it's neighbours ("d" here). Now the stack looks like    stack =  ["d","c"]
we pop and print "c", and add all it's neighbours ("e" here)... no neighbours are there. Now, stack =  ["e","d"]

Now we pop and print "d", and add it's neighbours ("f").  stack = ["f","e"]
Now we pop and print "e", and add it's neighbours (None).  stack = ["f"]
Now we pop and print "f", and add it's neighbours (it has none).  stack = []

at the end of this while loop, len(stack) == 0, and the loop breaks. So we come out of it and finish execution.
"""
def printBfs(graph,source):
    stack = collections.deque([source])

    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbour in graph[current]:
            stack.appendleft(neighbour)



graph = { "a" : ["b","c"],
          "b" : ["d"],
          "c" : ["e"],
          "d" : ["f"],
          "e" : [],
          "f" : []
        }
    
printBfs(graph,"a")

