from aoc.solution import SolutionABC

class Solution4(SolutionABC):
    def __init__(self, content: str) -> None:
        self.parsed = [([*map(int, elf1.split("-"))], [*map(int, elf2.split("-"))]) for elf1, elf2 in [line.split(",") for line in content.splitlines()]]

    def range_contains(self, range1: range, range2: range) -> bool:
        return all(e in range2 for e in range1) or all(e in range1 for e in range2)

    def range_overlaps(self, range1: range, range2: range) -> bool:
        return any(e in range2 for e in range1)

    def part_one(self) -> str | int:
        pairs = 0
        for (elf1_start, elf1_end), (elf2_start, elf2_end) in self.parsed:
            elf1_range = range(elf1_start, elf1_end + 1)
            elf2_range = range(elf2_start, elf2_end + 1)
            if self.range_contains(elf1_range, elf2_range):
                pairs += 1
        return pairs
    def part_two(self) -> str | int:
        pairs = 0
        for (elf1_start, elf1_end), (elf2_start, elf2_end) in self.parsed:
            elf1_range = range(elf1_start, elf1_end + 1)
            elf2_range = range(elf2_start, elf2_end + 1)
            if self.range_overlaps(elf1_range, elf2_range):
                pairs += 1
            print("-"*30)
        return pairs
