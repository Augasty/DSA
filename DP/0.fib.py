# Time: O(2^N) | Space: O(N)
def fib(n: int):
    if n == 1 or n == 2: return 1
    return fib(n - 1) + fib(n - 2)

# Memoization | Time: O(N) | Space: O(N)
def fib_memo(n: int, mem = {}): 
    if n in mem: return mem[n]
    if n == 1 or n == 2: return 1
    mem[n] = fib(n - 1)  + fib(n - 2)
    return mem[n]

# Tabulation | Time: O(N) | Space: O(N)
def fib_tab(n: int): 
    dp = [1 for i in range(n)]
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]  
