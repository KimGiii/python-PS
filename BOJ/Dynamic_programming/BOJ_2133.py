from sys import stdin
input = stdin.readline

n = int(input())
dp = [0] * (n + 1)

if n == 1:
    print(0)
else:
    dp[2] = 3
    for i in range(4, n + 1):
        if i % 2 == 0:
            dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2]) * 2 + 2
        else:
            dp[i] = 0

    print(dp[n])