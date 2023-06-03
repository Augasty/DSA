def isPrefix(target: str, prefix: str):
    if len(prefix) > len(target): return False
    for i in range(len(prefix)):
        if target[i] != prefix[i]:
            return False
    return True

# Time: O(len(words) ^ len(target) * len(target)) | Space: O(len(target) * len(target))
def countConstruct(target: str, prefixes: list):
    if target == "": return 1
    res = 0
    for prefix in prefixes:
        if isPrefix(target, prefix):
            res += countConstruct(target[len(prefix):], prefixes)
    return res
    
# Memoization | Time: O(len(words) * len(target) * len(target)) | Space: O(len(target) * len(target))
def countConstructMem(target: str, prefixes: list, mem: dict):
    if target == "": return 1
    if target in mem: return mem[target]
    res = 0
    for prefix in prefixes:
        if isPrefix(target, prefix):
            res += countConstructMem(target[len(prefix):], prefixes, mem)
    mem[target] = res
    return res

# Tabulation | Time: O(len(words) * len(target) * len(target)) | Space: O(len(target))
def countConstructTab(target: str, prefixes: list):
    dp = {target[i:]: 0 for i in range(len(target) + 1)}
    dp[target] = 1
    for word in dp:
        for prefix in prefixes:
            if isPrefix(word, prefix) and dp[word] > 0:
                dp[word[len(prefix):]] += dp[word]
    return dp[""]

print(countConstructTab("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstructTab("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstructTab("stakeboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstructTab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstructTab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))