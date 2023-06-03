# Time: O(2 ^ (m + n)) | Space: O(m + n)
def gridTraveler(n: int, m: int):
    if n == 0 or m == 0: return 0
    if n == 1 and m == 1: return 1
    return gridTraveler(n - 1, m) + gridTraveler(n, m - 1)

# Memoization | Time: O(m * n) | Space: O(m + n)
def gridTravelerMemo(n: int, m: int, mem = {}): 
    if n == 0 or m == 0: return 0
    if n == 1 and m == 1: return 1
    if (n, m) in mem: return mem[(n, m)]
    if (m, n) in mem: return mem[(m, n)]
    mem[(n, m)] = gridTravelerMemo(n - 1, m) + gridTravelerMemo(n, m - 1)
    return mem[(n, m)]

# Tabulation | Time: O(m * n) | Space: O(m * n)
def gridTravelerTab(n: int, m: int):
    dp = [[0 for i in range(m)] for i in range(n)]
    dp[0][0] = 1
    for i in range(0, n):
        for j in range(0, m):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]    
    return dp[n - 1][m - 1]
