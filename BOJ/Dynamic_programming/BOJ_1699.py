"""
문제 : 주어진 수를 제곱 수의 합으로 나타내서, 최소 항의 개수를 구하라
1의 제곱 = 1
2의 제곱 = 4
3의 제곱 = 9
4의 제곱 = 16
...
316의 제곱 = 99856
"""

from sys import stdin
readline = stdin.readline

# 라그랑주의 네 제곱수 정리에 의해, 모든 자연수는 최대 4개의 제곱수 합으로 표현 가능
def min_square_sum(n):
    # 제곱수인 경우 1 반환
    if int(n ** 0.5) ** 2 == n:
        return 1

    # 두 제곱수의 합으로 표현 가능한지 확인
    for i in range(1, int(n ** 0.5) + 1):
        if int((n - i ** 2) ** 0.5) ** 2 == n - i ** 2:
            return 2

    # n = 4^k * (8*m + 7) 형태인지 확인 (이 경우 항상 4개의 제곱수 필요)
    temp = n
    while temp % 4 == 0:
        temp //= 4
    if temp % 8 == 7:
        return 4

    # 그 외의 경우는 모두 3개의 제곱수로 표현 가능
    return 3

x = int(readline())
print(min_square_sum(x))