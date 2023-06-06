def isPrefix(target: str, prefix: str):
    if len(prefix) > len(target):
        return False
    for i in range(len(prefix)):
        if target[i] != prefix[i]:
            return False
    return True


def allConstructTab(target: str, prefixes: list):
    dp = [[] for i in range(len(target) + 1)]
    dp[0] = [[]]

    for idx in range(len(target)+1):
        for word in prefixes:
            if target[idx:idx+len(word)] == word:
                for array in dp[idx]:  #dp[idx] is an array of arrays,
                    temp = array + [word]    # we are adding [word] in every array of it
                    print(temp)
                    dp[idx + len(word)].append(temp) #and appending it to dp[idx + len(word)]
    
    return dp[-1]


# print(allConstructTab("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(allConstructTab("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# print(allConstructTab("stakeboard", [
#       "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstructTab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))