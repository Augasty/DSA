def isPrefix(target: str, prefix: str):
    if len(prefix) > len(target): return False
    for i in range(len(prefix)):
        if target[i] != prefix[i]:
            return False
    return True

# Time: O(len(words) ^ len(target) * len(target)) | Space: O(len(target) * len(target))
def canConstruct(target: str, prefixes: list):
    if target == "": return True
    for prefix in prefixes:
        if isPrefix(target, prefix) and canConstruct(target[len(prefix):], prefixes):
            return True
    return False

# Memoization | Time: O(len(words) * len(target) * len(target)) | Space: O(len(target) * len(target))
def canConstructMem(target: str, prefixes: list, mem: dict):
    if target == "": return True
    if target in mem: return mem[target]
    for prefix in prefixes:
        if isPrefix(target, prefix) and canConstructMem(target[len(prefix):], prefixes, mem):
            mem[target] = True
            return True
    mem[target] = False
    return False
    
# Tabulation | Time: O(len(words) * len(target) * len(target)) | Space: O(len(target))
def canConstructTab(target: str, prefixes: list):
    dp = {target[i:]: False for i in range(len(target) + 1)}
    dp[target] = True
    for word in dp:
        for prefix in prefixes:
            if dp[word] and isPrefix(word, prefix):
                dp[word[len(prefix):]] = True
    return dp[""]
  
    
print(canConstructTab("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstructTab("stakeboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstructTab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstructTab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))