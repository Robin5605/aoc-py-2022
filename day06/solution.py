from aoc.solution import SolutionABC

def check_duplicates(string: str) -> bool:
    return not all(string.count(c) == 1 for c in string)

class Solution6(SolutionABC):
    def __init__(self, content: str) -> None:
        self.content = content

    def part_one(self) -> str | int:
        for i, char in enumerate(self.content[:-3]):
            slice = self.content[i:i+4]
            if not check_duplicates(slice):
                return i + 4

    def part_two(self) -> str | int:
        for i, char in enumerate(self.content[:-13]):
            slice = self.content[i:i+14]
            if not check_duplicates(slice):
                return i + 14
