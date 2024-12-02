# https://adventofcode.com/2024/day/1#part2
# Run: cat 1/input.txt | python3 1/1-p2.py

import sys
from typing import List

def similarity_score(left: List[int], right: List[int]) -> int:
    return sum(a * right.count(a) for a in left)

def main():
    left = []
    right = []
    for line in sys.stdin:
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)
    print(similarity_score(left, right))

if __name__ == '__main__':
    main()
