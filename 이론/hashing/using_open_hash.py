from enum import Enum
from open_hash import OpenHash

Menu2 = Enum('menu2', ['추가', '삭제', '검색', '덤프', '종료'])

def select_menu() -> Menu2:
    """메뉴 선택"""
    s = [f'({m.value}) {m.name}' for m in Menu2]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu2):
            return Menu2(n)

hash = OpenHash(13)

while True:
    menu2 = select_menu()

    if menu2 == Menu2.추가:
        key = int(input('추가할 키: '))
        val = int(input('추가할 값: '))
        if not hash.add(key, val):
            print('추가 실패!')

    elif menu2 == Menu2.삭제:
        key = int(input('삭제할 키: '))
        if not hash.remove(key):
            print('삭제 실패!')

    elif menu2 == Menu2.검색:
        key = int(input('검색할 키: '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값 = {t}')
        else:
            print('검색 실패!')

    elif menu2 == Menu2.덤프:
        hash.dump()

    else:
        break