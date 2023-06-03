s = "abc"
# list of all the partitioning list
res = []
part = []
def dfs(i):
    if i >= len(s):
        res.append(part.copy())
        return
    for x in range(i,len(s)):
        part.append(s[i:x+1])
        dfs(x+1)
        part.pop()

dfs(0)

print(res)