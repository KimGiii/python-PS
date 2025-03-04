# 증가하는 부분 수열에서 합이 가장 큰 것을 구하는 프로그램 작성
# 그러면 먼저 증가하는 부분 수열을 찾고
# 그것들의 합을 비교?
import sys
input=sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [0 for _ in range(1001)]

for i in nums:
    dp[i] = max(dp[:i]) + i
print(max(dp))