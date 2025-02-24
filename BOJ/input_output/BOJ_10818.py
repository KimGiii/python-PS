import sys
input = sys.stdin.readline

# 시간 : 596 ms / 메모리 : 132864 kb
# n = int(input())
# arr = list(map(int, input().split()))
#
# if len(arr) != n:
#     print('error')
# else:
#     arr.sort()
#     print(arr[0], arr[-1])

# 시간 : 316ms / 메모리 : 131840kb
n = int(input())
arr = list(map(int, input().split()))

print(min(arr), max(arr))