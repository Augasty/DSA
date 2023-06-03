def isPrefix(target: str, prefix: str):
    if len(prefix) > len(target): return False
    for i in range(len(prefix)):
        if target[i] != prefix[i]:
            return False
    return True

# Time: O(len(words) ^ len(target) * len(target)) | Space: O(len(target) * len(target))
def allConstruct(target: str, prefixes: list):
    if target == "": return [[]]
    res = []
    for prefix in prefixes:
        if isPrefix(target, prefix):
            pos = allConstruct(target[len(prefix):], prefixes)
            for p in pos:
                p += [prefix]
                res.append(p)
    return res

# Memoization | Time: O(len(words) * len(target) * len(target)) | Space: O(len(target) * len(target))
def allConstructMem(target: str, prefixes: list, mem: dict):
    if target == "": return [[]]
    if target in mem: return mem[target]
    res = []
    for prefix in prefixes: 
        if isPrefix(target, prefix):
            pos = allConstructMem(target[len(prefix):], prefixes, mem)
            for p in pos:
                p += [prefix]
                res.append(p)
    mem[target] = res
    return res

# Tabulation | Time: O(len(words) * len(target) * len(target)) | Space: O(len(target))
def allConstructTab(target: str, prefixes: list):
    dp = {target[i:]: [] for i in range(len(target) + 1)}
    dp[target] = [[]]
    for word in dp:
        for prefix in prefixes:
            if isPrefix(word, prefix):
                for pos in dp[word]:
                    pos = pos.copy()
                    pos.append(prefix)
                    dp[word[len(prefix):]].append(pos)
    return dp[""]
                
print(allConstructTab("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstructTab("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstructTab("stakeboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstructTab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
                
