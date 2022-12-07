from __future__ import annotations
from aoc.solution import SolutionABC
from typing import TypeVar, Sequence

T = TypeVar('T')

class SimpleStack:
    def __init__(self) -> None:
        self.list: list[T] = []

    @classmethod
    def from_sequence(cls, seq: Sequence) -> SimpleStack:
        s = cls()
        for i in seq:
            s.push(i)
        return s

    def push(self, item: T) -> None:
        self.list.append(item)

    def pop(self) -> T:
        return self.list.pop()

    def is_empty(self) -> bool:
        return len(self.list) == 0


class Solution5(SolutionABC):
    def __init__(self, contents: str) -> None:
        self.contents = contents
        # Hard coding today's input
        stacks = [
            'ZJG',
            'QLRPWFVC',
            'FPMCLGR',
            'LFBWPHM',
            'GCFSVQ',
            'WHJZMQTL',
            'HFSBV',
            'FJZS',
            'MCDPFHBT',
        ]

        self.stacks = [SimpleStack.from_sequence(s) for s in stacks]
        self.instructions = [self.parse_line(s.strip()) for s in contents.strip().split("\n\n")[1].split("\n")]

    def parse_line(self, line: str) -> tuple[int, int, int]:
        new = line.replace("move ", "").replace("from ", "").replace("to ", "").strip()
        return tuple(map(int, new.split(" ")))

    def part_one(self) -> str | int:
        self.__init__(self.contents) # Reset stacks
        for crates, source, target in self.instructions:
            target_stack = self.stacks[target - 1]
            source_stack = self.stacks[source - 1]
            for _ in range(crates):
                target_stack.push(source_stack.pop())
        
        return "".join(stack.pop() for stack in self.stacks)

    def part_two(self) -> str | int:
        self.__init__(self.contents) # Reset stacks
        for crates, source, target in self.instructions:
            target_stack = self.stacks[target - 1]
            source_stack = self.stacks[source - 1]
            temp = SimpleStack()
            for _ in range(crates):
                temp.push(source_stack.pop())
            while not temp.is_empty():
                target_stack.push(temp.pop())
        
        return "".join(stack.pop() for stack in self.stacks)
