def bestSumTab(nums: list, target: int):
    dp = [None for i in range(target + 1)]
    dp[0] = []
    for n in nums:
        for i in range(len(dp)):
            if dp[i]!=None and i+n < len(dp) and dp[i+n] == None:
                dp[i+n] = dp[i] + [n]
        print(dp)
    return dp[-1]


print(bestSumTab([2, 3, 5], 8))