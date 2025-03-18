from sys import stdin
input = stdin.readline

n = int(input())
nums = []
for i in range(n):
    a, b = list(map(int, input().split()))
    nums.append((b, a))

nums.sort()

for b, a in nums:
    print(a, b)