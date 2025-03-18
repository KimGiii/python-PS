from sys import stdin
input = stdin.readline

card = int(input())
cost = list(map(int, input().split()))
dp = [0 for _ in range(card + 1)]
dp[1] = cost[0]

for i in range(2, card + 1):
    max_cost = cost[i - 1]
    for j in range(1, i//2 + 1):
        price = dp[i - j] + dp[j]
        if price > max_cost:
            max_cost = price
    dp[i] = max_cost

print(dp[card])