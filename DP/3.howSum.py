# Time: O(len(nums) ^ target * target) | Space: O(target)
def howSum(target: int, nums: list):
    if target == 0: return []
    if target < 0: return None
    for num in nums:
        pos = howSum(target - num, nums)
        if pos != None:
            pos += [num]
            return pos
    return None

# Memoization | Time: O(len(nums) * target * target) | Space: O(target * target)
def howSumMem(target: int, nums: list, mem: dict):
    if target == 0: return []
    if target < 0: return None
    if target in mem: return mem[target]
    for num in nums:
        pos = howSumMem(target - num, nums, mem)
        if pos != None:
            pos += [num]
            mem[target] = pos
            return pos
    mem[target] = None
    return None

# Tabulation | Time: O(len(nums) * target * target) | Space: O(target * target)
def howSumTab(target: int, nums: list):
    dp = [None for i in range(target + 1)]
    dp[0] = []
    for num in nums:
        for i in range(len(dp)):
            if dp[i] != None and i + num < len(dp):
                dp[i + num] = dp[i] + [num]
    return dp[-1]
                
            
# print(howSumTab(7, [2, 1]))
# print(howSumTab(7, [5, 3, 4, 7]))
# print(howSumTab(7, [2, 4]))
# print(howSumTab(8, [3, 5, 2]))
# print(howSumTab(300, [7, 14]))
