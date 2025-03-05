import bisect
import sys
input = sys.stdin.readline

# 입력 처리
n = int(input())
arr = list(map(int, input().split()))
# 배열 역순으로 뒤집어 -> 왜?
# 역으로 뒤에서부터 오름차순으로 증가하는 배열을 찾으면 되니까
# reversed_arr = arr[::-1]
dp = []

for i in arr:
    # 배열 값에 마이너스(-)를 붙이면 배열이 뒤집히는 효과가 안나나?
    # 나는듯?
    val = -i
    p = bisect.bisect_left(dp, val)
    if p == len(dp):
        dp.append(val)
    else:
        dp[p] = val

# print(dp)
print(len(dp))