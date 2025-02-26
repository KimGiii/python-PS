n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    # 규칙 : 3번째부터 앞에 두 개의 합
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])