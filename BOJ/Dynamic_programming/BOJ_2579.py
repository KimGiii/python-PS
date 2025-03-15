"""

문제: 마지막 계단에 도착했을 때, 가장 점수가 높을 경우 출력

규칙1. 계단은 1칸 또는 두칸 갈 수 있다
규칙2. 연속된 3개를 밟을 수는 없다. 단 시작점은 계단에 포함X
규칙3. 마지막 계단은 반드시 밟아야한다.

"""

from sys import stdin
input = stdin.readline

n = int(input())
dp = [0] * 10000
a = [0] * 10000
for i in range(1, n+1):
    a[i] = int(input())

dp[1] = a[1]
dp[2] = a[1] + a[2]
dp[3] = max(a[1] + a[3], a[2] + a[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-2] + a[i], dp[i-3] + a[i-1] + a[i])

print(dp[n])