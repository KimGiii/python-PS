from sys import stdin
input = stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort()
for i in range(n):
    print(a[i][0], a[i][1])