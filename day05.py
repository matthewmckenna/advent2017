#!/usr/bin/env python3
"""
Day 5 of Advent of Code 2017
http://adventofcode.com/2017/day/5
"""
from typing import List


def jump_list_steps(sequence: List[int]) -> int:
    """Compute number of steps needed to escape list."""
    current_idx = steps = 0

    within_sequence = True

    while within_sequence:
        jump_by = sequence[current_idx]

        # update the previous value before we jump
        sequence[current_idx] += 1

        current_idx += jump_by

        steps += 1

        if current_idx > len(sequence) - 1:
            # we're outside of the sequence
            within_sequence = False
            break

    return steps


def jump_list_steps_part2(sequence: List[int]) -> int:
    """Compute the number of steps needed to escape the list for part two."""
    current_idx = steps = 0
    within_sequence = True

    while within_sequence:
        jump_by = sequence[current_idx]

        if sequence[current_idx] >= 3:
            sequence[current_idx] -= 1
        else:
            sequence[current_idx] += 1

        current_idx += jump_by

        steps += 1

        if current_idx > len(sequence) - 1:
            within_sequence = False
            break

    return steps


if __name__ == '__main__':
    with open('data/day05.txt', 'rt') as f:
        data = [int(x) for x in f]

    assert jump_list_steps([0, 3, 0, 1, -3]) == 5
    assert jump_list_steps_part2([0, 3, 0, 1, -3]) == 10

    # send a copy of data as we mutate within this function
    print(jump_list_steps(data[:]))
    print(jump_list_steps_part2(data))
