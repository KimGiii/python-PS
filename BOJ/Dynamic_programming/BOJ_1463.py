l = {}
def f(x):
    if x in l:
        return l[x]
    # x가 1이하면 연산할 필요 없으므로 0 반환
    if x <= 1:
        return 0
    # 3으로 나누기 전, 나머지만큼 빼고 그 후에 1번의 연산을 한 뒤 남은 숫자에 대해 재귀호출
    d1 = f(x//3) + x % 3 + 1
    # 2로 나누기 전, 나머지만큼 빼고 그 후에 1번의 연산을 한 뒤 남은 숫자에 대해 재귀호출
    d2 = f(x//2) + x % 2 + 1
    # 두 경우 중 더 작은 연산 횟수를 선택
    result = min(d1, d2)
    l[x] = result

    return result

n = int(input())
print(f(n))