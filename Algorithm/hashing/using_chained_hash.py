# chaining으로 구현된 ChainedHash 사용

from enum import Enum
from problem_solving.Algorithm.hashing.chained_hash import ChainedHash

# 메뉴 선언
Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'{m.value}{m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


# 크기가 13인 hash table 생성
hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.추가:
        key = int(input('추가할 키: '))
        val = int(input('추가할 값: '))
        if not hash.add(key, val):
            print('추가 실패')

    elif menu == Menu.삭제:
        key = int(input('삭제할 키: '))
        if not hash.remove(key):
            print('삭제 실패')

    elif menu == Menu.검색:
        key = int(input('검색할 키: '))
        t = hash.search(key)
        if t is not None:
            print(f"검색한 키 값을 같은 값 = {t}")
        else:
            print('검색할 데이터 없음')

    elif menu == Menu.덤프:
        hash.dump()

    else:
        print('종료!')
        break