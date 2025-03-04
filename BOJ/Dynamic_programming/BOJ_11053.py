import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]
dp_idx = 0

def search(l, r, t):
    while l < r:
        mid = (l + r) // 2
        if dp[mid] < t:
            l = mid + 1
        else:
            r = mid
    return l

for i in range(1, n):
    if dp[dp_idx] < nums[i]:
        dp.append(nums[i])
        dp_idx += 1

    else:
        idx = search(0, dp_idx, nums[i])
        dp[idx] = nums[i]

print(dp_idx+1)