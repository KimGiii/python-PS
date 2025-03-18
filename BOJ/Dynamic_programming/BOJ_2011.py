from sys import stdin
input = stdin.readline

# 인덱스를 맞추기 위한 초기값
code = [0]
code += list(input())
# '\n' 날리기 위해 pop
code.pop()

# 0으로 시작할 때 오류 발생
if code[1] == '0':
    print(0)
    exit(0)

dp = [0] * len(code)
dp[0] = dp[1] = 1

for i in range(2, len(code)):
    # 한자리 수를 나타내기 위해서
    ones = int(code[i])
    # 두자리 수를 나타내기 위해서
    tens = int(code[i - 1]) * 10 + int(code[i])

    if ones > 0:
        dp[i] += dp[i - 1]
    if 10 <= tens <= 26:
        dp[i] += dp[i - 2]

print(dp[-1] % 1000000)