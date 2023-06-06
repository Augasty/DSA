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
def countConstructMem(target,prefixes,memo=None):
    if memo is None:
        memo ={}

    if target == '':
        return 1
    if target in memo:
        return memo[target]
    result = 0
    for ele in prefixes:
        if isPrefix(target,ele):
            substring_result = countConstructMem(target[len(ele):],prefixes,memo)
            result += substring_result
    memo[target] = result
    return result

# Tabulation | Time: O(len(words) * len(target) * len(target)) | Space: O(len(target))
def countConstructTab(target: str, prefixes: list):
    dp = [0 for i in range(len(target) + 1)]

    dp[0] = 1
    for idx in range(len(dp)):
        for prefix in prefixes:
            if target[idx:idx+len(prefix)] == prefix:
                dp[idx+len(prefix)] += dp[idx]
    return dp[-1]


print(countConstructTab("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstructMem("stakeboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstructMem("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstructMem("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
