import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    x = int(input())
    dp = [0, 1, 2, 4]

    for j in range(4, x+1):
        dp.append(dp[j-1] + dp[j-2] + dp[j-3])

    print(dp[x])