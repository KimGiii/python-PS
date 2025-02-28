# 규칙1. 0으로 시작하지 않는다.
# 규칙2. 11을 부분문자열로 갖지 않는다.

n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1])