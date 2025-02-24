# 고정 길이 큐 사용하기

from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['Enque', 'Deque', 'Peek', 'Find', 'Dump', 'End'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}) {m.name}' for m in Menu]
    while True:
        print(*s, sep = ' ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f'현재 데이터 개수 : {len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.Enque:
        x = int(input('인큐할 데이터 입력 : '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('Full queue')

    elif menu == Menu.Deque:
        try:
            x = q.deque()
            print(f'디큐한 데이터 : {x}')
        except FixedQueue.Empty:
            print('Empty queue')

    elif menu == Menu.Peek:
        try:
            x = q.peek()
            print(f'피크한 데이터 : {x}')
        except FixedQueue.Empty:
            print('Empty queue')

    elif menu == Menu.Find:
        x = int(input('검색할 값 입력 : '))
        if x in q:
            print(f'{q.count(x)} 개 포함, 맨 앞의 위치 = {q.find(x)}')
        else:
            print('Not found')

    elif menu == Menu.Dump:
        q.dump()

    else:
        print('Test end!')
        break