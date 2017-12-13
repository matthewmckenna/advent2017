#!/usr/bin/env python3
"""
Day 6 of Advent of Code 2017
http://adventofcode.com/2017/day/6
"""
import operator
from typing import Dict, List, Set


def count_cycles(sequence: List[int]) -> int:
    """Count the number of redistribution cycles.

    Count the number of redistribution cycles before we encounter
    input that we've previously seen.
    """
    cycles = 0
    all_unique_memory = True
    seen: Set[str] = set()

    while all_unique_memory:
        # find the maximum value, and the index.
        max_idx, max_value = max(enumerate(sequence), key=operator.itemgetter(1))

        # zero the max_value
        sequence[max_idx] = 0

        # iterate through this value and add one to each other value
        redist_start_idx = (max_idx+1) % len(sequence)

        for _ in range(max_value):
            sequence[redist_start_idx] += 1

            redist_start_idx = (redist_start_idx+1) % len(sequence)

        cycles += 1

        str_sequence = ''.join((str(s) for s in sequence))

        if str_sequence not in seen:
            seen.add(str_sequence)
        else:
            break

    return cycles


def count_cycle_length(sequence: List[int]) -> int:
    """Count the length of the loop in the cycle."""
    cycle = cycle_length = 0
    all_unique_memory = True
    seen: Dict[str, int] = {}

    while all_unique_memory:
        # find the maximum value, and the index.
        max_idx, max_value = max(enumerate(sequence), key=operator.itemgetter(1))

        # zero the max_value
        sequence[max_idx] = 0

        # iterate through this value and add one to each other value
        redist_start_idx = (max_idx+1) % len(sequence)

        for _ in range(max_value):
            sequence[redist_start_idx] += 1

            redist_start_idx = (redist_start_idx+1) % len(sequence)

        str_sequence = ''.join((str(s) for s in sequence))

        if str_sequence not in seen:
            seen[str_sequence] = cycle
        else:
            cycle_length = cycle - seen[str_sequence]
            break

        cycle += 1

    return cycle_length


if __name__ == '__main__':
    with open('data/day06.txt', 'rt') as f:
        data = [int(x) for x in f.read().split('\t')]

    assert count_cycles([0, 2, 7, 0]) == 5
    assert count_cycle_length([0, 2, 7, 0]) == 4

    print(count_cycles(data))
    print(count_cycle_length(data))
