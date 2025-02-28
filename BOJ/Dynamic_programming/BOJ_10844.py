import sys
input = sys.stdin.readline
MOD = 1000000000

n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][1] % MOD
    dp[i][9] = dp[i - 1][8] % MOD
    for k in range(1, 9):
        dp[i][k] = (dp[i - 1][k - 1] + dp[i - 1][k + 1]) % MOD

print(sum(dp[n]) % MOD)