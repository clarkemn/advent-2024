# https://adventofcode.com/2024/day/2
# Run: cat 3/input.txt | python 3/3-p2.py


import sys
import re

def find_valid_pattern(text):
    # Define the pattern regex
    pattern = re.compile(r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))")
    matches = pattern.findall(text)
    return matches

def main():
    total = 0
    text = sys.stdin.read()
    matches = find_valid_pattern(text)
    mul_enabled = True  # At the beginning, mul instructions are enabled

    for match in matches:
        if match[0] == "do()":
            mul_enabled = True
        elif match[0] == "don't()":
            mul_enabled = False
        elif mul_enabled and match[1] and match[2]:
            x, y = int(match[1]), int(match[2])
            total += x * y

    print(total)

if __name__ == '__main__':
    main()
