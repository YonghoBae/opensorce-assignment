from typing import Any

# stack.py
class FixedStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ptr = 0
        self.stack = [None] * capacity

    def is_empty(self) -> bool:
        return self.ptr == 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value) -> None:
        if self.is_full():
            raise OverflowError("스택이 가득 찼습니다.")
        self.stack[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("스택이 비어 있습니다.")
        self.ptr -= 1
        return self.stack[self.ptr]

