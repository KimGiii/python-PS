# 고정 길이 스택 클래스 사용

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['push', 'pop', 'peek', 'find', 'dump', 'end'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}) {m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)

while True:
    print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.push:
        x = int(input('데이터 입력 : '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('Full Stack')

    elif menu == Menu.pop:
        try:
            x = s.pop()
            print(f'데이터: {x}')
        except FixedStack.Empty:
            print('Empty Stack')

    elif menu == Menu.peek:
        try:
            x = s.peek()
            print(f'데이터: {x}')
        except FixedStack.Empty:
            print('Empty Stack')

    elif menu == Menu.find:
        x = int(input('검색할 값 입력 : '))
        if x in s:
            print(f'{s.count(x)}개 포함, 맨 앞의 위치는 {s.find(x)}')
        else:
            print('Not found')

    elif menu == Menu.dump:
        s.dump()

    else:
        print('Test end!')
        break