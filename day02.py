#!/usr/bin/env python3
"""
Day 2 of the Advent of Code 2017 challenge.
"""
import itertools
from typing import List

from aoc_utils import read_tsv


def corruption_checksum(data: List[List[int]]) -> int:
    """Compute a checksum as the sum of the max-min in each line."""
    checksum = 0
    for seq in data:
        checksum += max(seq) - min(seq)
    return checksum


def sum_even_divisions(data: List[List[int]]) -> int:
    """Sum the result of the only even division on each line."""
    # for seq in data:
    #     for i, j in itertools.permutations(seq, 2):
    #         if (i % j) == 0:
    #             total += int(i/j)
    #             break
    return sum(
        int(i/j)
        for seq in data
        for i, j in itertools.permutations(seq, 2)
        if (i % j == 0)
    )


if __name__ == '__main__':
    data = read_tsv('data/day02.txt')
    # data = read_tsv('data/day02_sample2.txt')
    # convert the string values to integers
    int_data = [[int(v) for v in row] for row in data]

    # print(corruption_checksum(int_data))
    print(sum_even_divisions(int_data))
