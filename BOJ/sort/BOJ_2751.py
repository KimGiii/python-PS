n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
a = [int(input()) for _ in range(n)]
a.sort()

for i in range(n):
    print(a[i])