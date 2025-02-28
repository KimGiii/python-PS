import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    x = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    # 입력 오류 처리
    if x<1 or x>100000:
        print('Invalied input')
    if x > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for j in range(2, n):
        dp[0][j] += max(dp[1][j-1], dp[1][j-2])
        dp[1][j] += max(dp[0][j-1], dp[0][j-2])

    result = max(dp[0][n-1], dp[1][n-1])
    sys.stdout.write(str(result))
