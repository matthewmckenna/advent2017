#!/usr/bin/env python3
"""
Day 4 of Advent of Code 2017
http://adventofcode.com/2017/day/4
"""
from collections import Counter
from typing import Iterable

from aoc_utils import yield_lines


def count_valid_passphrases(lines: Iterable[str]) -> int:
    num_valid = 0

    for line in lines:
        c = Counter(line.split())
        if all(x == 1 for x in c.values()):
            num_valid += 1

    return num_valid


def count_valid_inc_anagrams(lines: Iterable[str]) -> int:
    num_valid = 0

    for line in lines:
        c = Counter([''.join(sorted(word)) for word in line.split()])
        if all(x == 1 for x in c.values()):
            num_valid += 1

    return num_valid


if __name__ == '__main__':
    lines = yield_lines('data/day04.txt')
    print(count_valid_passphrases(lines))

    lines = yield_lines('data/day04.txt')
    print(count_valid_inc_anagrams(lines))
