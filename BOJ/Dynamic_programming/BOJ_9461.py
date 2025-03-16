from sys import stdin
input = stdin.readline

test_number = int(input())

for i in range(test_number):
    case = int(input())
    dp = [1 for _ in range(case)]

    if case >= 2:
        dp[1] = 1
    if case >= 3:
        dp[2] = 1
    if case >= 4:
        dp[3] = 2
    if case >= 5:
        dp[4] = 2

    for j in range(5, case):
        dp[j] = dp[j - 5] + dp[j - 1]

    print(dp[-1])