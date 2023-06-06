# PROBLEM: Say that you are a traveler on a 2D grid. You begin in the
# top-left corner and your goal is to travel to the bottom-right corner.
# You may only move down or right.
# In how many ways can you travel to the goal on a grid with dimensions m * n?


# Time: O(2 ^ (m + n)) | Space: O(m + n)
def gridTraveler(n: int, m: int):
    if n == 0 or m == 0:
        return 0
    if n == 1 and m == 1:
        return 1
    return gridTraveler(n - 1, m) + gridTraveler(n, m - 1)

# Memoization | Time: O(m * n) | Space: O(m + n)


def gridTravelerMemo(m: int, n: int, mem=None):
    if mem is None:  
        mem = {}
        
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    if (m, n) in mem:
        return mem[(m, n)]
    mem[(n, m)] = gridTravelerMemo(m, n - 1) + gridTravelerMemo(m - 1, n)
    return mem[(n, m)]

# Tabulation | Time: O(m * n) | Space: O(m * n)


def gridTravelerTab(m: int, n: int):
    dp = [[0 for i in range(n)] for i in range(m)]
    dp[0][0] = 1
    for i in range(0, m):
        for j in range(0, n):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[m - 1][n - 1]


print(gridTraveler(2, 2))
print(gridTravelerTab(13, 14))