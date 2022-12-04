from aoc.solution import SolutionABC
from string import ascii_lowercase, ascii_uppercase
from itertools import islice

class Solution3(SolutionABC):
    def __init__(self, content: str) -> None:
        self.backpacks = content.strip().splitlines()

    def get_priority(self, letter: str) -> int:
        if letter in ascii_lowercase:
            return ascii_lowercase.index(letter) + 1

        if letter in ascii_uppercase:
            return ascii_uppercase.index(letter) + 1 + 26

    def chunker(self, seq: list[str], size: int) -> list[list[str]]:
        it = iter(seq)
        while (chunk := list(islice(it, size))):
            yield chunk

    def find_common(self, *args: str) -> str:
        for letter in args[0]:
            if all(letter in other for other in args[1:]):
                return letter

    def part_one(self) -> str | int:
        total = 0
        for backpack in self.backpacks:
            c = len(backpack) // 2
            compartment_one = backpack[:c]
            compartment_two = backpack[c:]

            common = self.find_common(compartment_one, compartment_two)
            total += self.get_priority(common)
        return total

    def part_two(self) -> str | int:
        groups = self.chunker(self.backpacks, 3)
        total = 0
        for group in groups:
            common = self.find_common(*group)
            priority = self.get_priority(common)
            total += priority
        return total
