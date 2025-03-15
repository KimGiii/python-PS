import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# 현재의 수가 이전 수랑 더한것보다 크면 현재의 수 선택, 아니면 더한 것 선택
for i in range(1, n):
    a[i] = max(a[i], a[i-1]+a[i])

print(max(a))