# https://adventofcode.com/2024/day/2
# Run: cat 3/input.txt | python 3/3-p1.py

import sys
import re

def find_valid_pattern(text):
    # Define the pattern regex
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = pattern.findall(text)
    return matches

def main():
    total = 0
    text = sys.stdin.read()
    matches = find_valid_pattern(text)
    # For each match, we need to multiply the two numbers and add it to the total
    for match in matches:
        x, y = map(int, match)
        total += x * y
    print(total)

if __name__ == '__main__':
    main()
