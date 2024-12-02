# https://adventofcode.com/2024/day/1
# Run: cat 1/input.txt | python3 1/1.py

import sys
from typing import List

# Helper function to calculate the distance between two lists
def distance_between_lists(left: List[int], right: List[int]) -> int:
    left.sort()
    right.sort()
    return sum(abs(a - b) for a, b in zip(left, right))

def main():
    left = []
    right = []
    for line in sys.stdin:
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)
    print(distance_between_lists(left, right))

if __name__ == '__main__':
    main()

# Run: cat 1/input.txt | python3 1/1.py