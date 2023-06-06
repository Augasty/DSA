def isPrefix(target: str, prefix: str):
    if len(prefix) > len(target):
        return False
    for i in range(len(prefix)):
        if target[i] != prefix[i]:
            return False
    return True

# Time: O(len(words) ^ len(target) * len(target)) | Space: O(len(target) * len(target))


def allConstruct(target: str, prefixes: list):
    if target == "":
        return [[]]
    res = []
    for prefix in prefixes:
        if isPrefix(target, prefix):
            pos = allConstruct(target[len(prefix):], prefixes)
            for p in pos:
                p += [prefix]
                res.append(p)
    return res

# Memoization | Time: O(len(words) * len(target) * len(target)) | Space: O(len(target) * len(target))


def allConstructMem(target: str, array: list, mem: dict = None):
    if mem is None:
        mem = {}
    if target == '':
        return [[]]

    if target in mem:
        return mem[target]
    result = []
    for ele in array:
        if isPrefix(target, ele):
            substring_result = allConstructMem(
                target[len(ele):], array, mem)  # retursn array of arrays
            for item in substring_result:
                item = [ele] + item
                result.append(item)
    mem[target] = result
    return result


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


print(allConstructMem("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstructMem("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstructMem("stakeboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstructTab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))