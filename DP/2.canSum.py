# Standard Time: O(len(nums) ^ target) | Space: O(target)
def canSum(nums: list, target: int):
    if target == 0: return True
    if target < 0: return False
    for num in nums:
        if canSum(nums, target - num):
            return True
    return False

# Memoization Time: O(len(nums) * target) | Space: O(target)
def canSumMem(nums: list, target: int, mem: dict):
    if target == 0: return True
    if target < 0: return False
    if target in mem: return mem[target]
    for num in nums:
        if canSumMem(nums, target - num, mem):
            mem[target] = True
            return True
    mem[target] = False
    return False

# Tabulation Time: O(len(nums) * target) | Space: O(target)
def canSumTab(nums: list, target: int):
    dp = [False for i in range(target + 1)]
    dp[0] = True
    for num in nums:
        for i in range(len(dp)):
            if dp[i] and i + num < len(dp):
                dp[i + num] = True
    return dp[-1]

# print(canSumTab([2, 3], 7))
# print(canSumTab([5, 3, 4, 7], 7))
# print(canSumTab([2, 4], 7))
# print(canSumTab([2, 3, 5], 8))
# print(canSumTab([7, 14], 300))
