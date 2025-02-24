# chaining으로 hash 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib


class Node:
    """hash를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:
    """chaining으로 hash 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""

        # hash table의 크기
        self.capacity = capacity
        # hash table을 저장하는 list형 배열
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        """hash 값을 구함"""
        if isinstance(key, int):
            return key % self.capacity

        # sha256 알고리즘: hashlib 모듈에서 제공하는 RSA의 FIPS 알고리즘을 바탕으로 해, 주어진 바이트 문자열의 hash value를 구하는 알고리즘의 생성자
        # encode() : sha256에 바이트 문자열의 인수를 전달하기 위해 key를 str형 문자열로 변환한뒤 바이트 문자열을 생성
        # hexdigest() : sha256 알고리즘에서 hash value를 16진수 문자열로 꺼냄
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""

        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        # 원소를 추가하는 과정
        # 1. hash function을 사용해 키를 hash 값으로 변환
        # 2. hash값을 인덱스로 하는 버킷에 주목
        # 3. 그 버킷이 참조하는 연결리스트를 맨 앞부터 차례로 선형검색, 키와 같은 값이 발견되면 추가 실패, 없으면 hash값인 리스트 맨 앞의 노드에 추가

        """키가 key이고 값이 value인 원소 추가"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True


    def remove(self, key: Any) -> bool:
        """키가 key인 원소 삭제"""

        # hash 값을 사용하여 키를 hash값으로 변환
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True

            pp = p
            p = p.next

        return False


    def dump(self) -> None:
        """hash table을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()