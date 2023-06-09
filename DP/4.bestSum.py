# Time: O(len(nums) ^ target * target) | Space: O(target)
def bestSum(nums: list, target: int):
    if target == 0:
        return []
    if target < 0:
        return None
    shortest = None
    for num in nums:
        pos = bestSum(nums, target - num)
        # if the result is not None, and
        if pos != None and (not shortest or len(pos) + 1 < len(shortest)):
            shortest = pos + [num]
    return shortest if shortest else None

# Memoization | Time: O(len(nums) * target * target) | Space: O(target * target)
def bestSumMem(nums: list, target: int, mem: dict = None):
    if mem is None:
        mem = {}

    if target == 0:
        return []
    if target < 0:
        return None
    if target in mem:
        return mem[target]
    shortest = None
    for num in nums:
        pos = bestSumMem(nums, target - num, mem)
        if pos != None and (not shortest or len(pos) + 1 < len(shortest)):
            shortest = pos + [num]
    if shortest:
        mem[target] = shortest
    else:
        mem[target] = None
    return mem[target]

# Tabulation | Time: O(len(nums) * target * target) | Space: O(target * target)


def bestSumTab(nums: list, target: int):
    dp = [None for i in range(target + 1)]
    dp[0] = []
    for num in nums:
        for i in range(len(dp)):
            if dp[i] != None and i + num < len(dp) and (dp[i + num] == None or len(dp[i]) + 1 < len(dp[i + num])):
                dp[i + num] = dp[i] + [num]
    return dp[-1]


def bestSumTab2(nums: list, target: int):
    dp = [None for i in range(target + 1)]
    dp[0] = []
    for i in range(len(dp)):
        for n in nums:
            if dp[i] != None and i+n < len(dp) and dp[i+n] == None:
                dp[i+n] = dp[i] + [n]  #this line also has a time complexity of target, becaue to unpack an array 
                # and add an element to it, we need to go through the array
        print(dp)
    return dp[-1]


print('answer is ', bestSumTab2([2, 3, 5], 8))
print(bestSumTab([2, 3], 7))
print(bestSumTab([5, 3, 4, 7], 7))
print(bestSumTab([2, 4], 7))
print(bestSumTab([2, 3, 5], 8))
print(bestSumTab([1, 4, 5], 8))
print(bestSumTab([1, 2, 5, 25], 100))
