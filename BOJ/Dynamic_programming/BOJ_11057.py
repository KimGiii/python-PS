import sys

MOD = 10007
dp = [1] * 10
n = int(input())

for i in range(1, n):
    for j in range(1, 10):
        dp[j] += dp[j-1]

result = str(sum(dp) % MOD)
sys.stdout.write(result)