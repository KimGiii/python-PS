"""
    바이토닉 수열
    1. 증가하는 부분 찾아
    2. 감소하는 수열 찾아
    3. 이때 두 수열을 합쳤을 때, 길이가 홀수여야함

"""

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
i_dp = [1] * n
d_dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and i_dp[i] < i_dp[j]+1:
            i_dp[i] = i_dp[j]+1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j] and d_dp[i] < d_dp[j]+1:
            d_dp[i] = d_dp[j]+1

result = 0
for i in range(n):
    result = max(result, i_dp[i] + d_dp[i] - 1)

print(result)