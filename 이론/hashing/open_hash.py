# 오픈 주소법으로 hash 함수 구현 하기

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷의 속성
class Status(Enum):
    # 데이터 저장
    OCCUPIED = 0
    # 비어 있음
    EMPTY = 1
    # 삭제 완료
    DELETED = 2

class Bucket:
    """hash를 구성하는 버킷"""

    def __init__(self, key: Any = None, value: Any = None,
                 stat: Status = Status.EMPTY) -> None:
        """초기화"""
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """모든 필드에 값 설정"""
        self.key = key
        self.value = value
        self.stat = stat

    def set_stat(self, stat: Status) -> None:
        """속성 설정"""
        self.stat = stat

class OpenHash:
    """오픈주소법으로 구현하는 hash 클래스"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> int:
        """hash 값 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)

    def rehash_value(self, key: Any) -> int:
        """rehash 값 구함"""
        return (self.hash_value(key) + 1) % self.capacity

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None

    def search_node(self, key: Any) -> Any:
        """키가 key인 버킷 검색"""
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return None

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소 추가"""
        if self.search(key) is not None:
            # 이미 등록된 키인 경우
            return False

        # 추가하는 키의 hash 값
        hash = self.hash_value(key)
        # 버킷을 주목
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            # rehash
            hash = self.rehash_value(hash)
            p = self.table[hash]
        # hash 테이블이 가득 찬 경우
        return False

    def remove(self, key: Any) -> int:
        """키가 key인 원소 삭제"""
        p = self.search_node(key)
        if p is None:
            # 등록되지 않은 키
            return False
        p.set_stat(Status.DELETED)
        return True

    def dump(self) -> None:
        """hash 테이블 덤프"""
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} -> {self.table[i].value}')
            elif self.table[i].stat == Status.EMPTY:
                print('미등록')
            elif self.table[i].stat == Status.DELETED:
                print('삭제 완료')