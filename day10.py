#!/usr/bin/env python3
"""
Day 10 of Advent of Code 2017.
http://adventofcode.com/2017/day/10
"""
from typing import Iterator, List, Tuple
import itertools

TEST_LIST = [0, 1, 2, 3, 4]
TEST_LENGTHS = [3, 4, 1, 5]


def reverse_section(sequence: List[int], idx: int, length: int) -> Iterator[Tuple[int, int]]:
    """Get the indices and reversed section of `sequence`."""
    # print(f'input: idx={idx} length={length} idx+length={idx+length}')

    if idx+length > len(sequence):
        excess = (idx+length) % len(sequence)
        selection = sequence[idx:] + sequence[:excess]
        indices = list(itertools.chain(range(idx, len(sequence)), range(excess)))
    else:
        selection = sequence[idx:idx+length]
        indices = list(range(idx, idx+length))

    reversed_selection = list(reversed(selection)) if selection else [sequence[idx]]

    # print(f'selection={selection} reversed={reversed_selection} indices={indices}')

    return zip(indices, reversed_selection)


def knot_hash(sequence: List[int], lengths: List[int]) -> int:
    idx = skip = 0
    sequence_length = len(sequence)
    # print(sequence)

    for knot_length in lengths:
        # print(f'idx={idx} knot_length={knot_length} skip={skip}')
        indices_section = reverse_section(sequence, idx, knot_length)

        for i, element in indices_section:
            sequence[i] = element

        idx = (idx+knot_length+skip) % sequence_length

        # print(f'sequence now {sequence}. new idx={idx}\n')

        skip += 1

    # print(sequence)
    return sequence[0]*sequence[1]


if __name__ == '__main__':
    with open('data/day10.txt', 'rt') as f:
        lengths = [int(length) for length in f.read().strip().split(',')]

    assert knot_hash(TEST_LIST, TEST_LENGTHS) == 12

    print(knot_hash(list(range(256)), lengths))
