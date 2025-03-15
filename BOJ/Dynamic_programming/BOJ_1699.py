"""
문제 : 주어진 수를 제곱 수의 합으로 나타내서, 최소 항의 개수를 구하라
1의 제곱 = 1
2의 제곱 = 4
3의 제곱 = 9
4의 제곱 = 16
...
316의 제곱 = 99856
"""

n = int(input())
dp = [i for i in range(n+1)]

# 제곱수를 기준으로 모든 경우를 계산, 최솟값을 저장
for i in range(2, n+1):
    for j in range(1, i+1):
        # 제곱수를 생성
        square = j * j
        if square > i:
            break

        if dp[i] > dp[i-square]+1:
            dp[i] = dp[i-square] + 1

print(dp[n])