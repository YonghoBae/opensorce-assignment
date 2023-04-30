class Stack:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.stack = [None] * capacity
        self.ptr = 0

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value) -> None:
        if self.is_full():
            raise OverflowError("Stack is full")
        self.stack[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        self.ptr -= 1
        return self.stack[self.ptr]

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self, value) -> int:
        for i in range(self.ptr - 1, -1, -1):
            if self.stack[i] == value:
                return i
        return -1

    def count(self, value) -> int:
        count = 0
        for i in range(self.ptr):
            if self.stack[i] == value:
                count += 1
        return count

    def __len__(self) -> int:
        return self.ptr

    def __contains__(self, value) -> bool:
        return self.count(value)
