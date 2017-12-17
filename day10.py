#!/usr/bin/env python3
"""
Day 10 of Advent of Code 2017.
http://adventofcode.com/2017/day/10
"""
import functools
import itertools
import operator
import string
from typing import Iterator, List, Tuple

from aoc_utils import sequence_blocks

TEST_LIST = [0, 1, 2, 3, 4]
TEST_LENGTHS = [3, 4, 1, 5]

CHAR_TO_ASCII = {char: ord(char) for char in string.printable}


def reverse_section(sequence: List[int], idx: int, length: int) -> Iterator[Tuple[int, int]]:
    """Get the indices and reversed section of `sequence`."""
    if idx+length > len(sequence):
        excess = (idx+length) % len(sequence)
        selection = sequence[idx:] + sequence[:excess]
        indices = list(itertools.chain(range(idx, len(sequence)), range(excess)))
    else:
        selection = sequence[idx:idx+length]
        indices = list(range(idx, idx+length))

    reversed_selection = list(reversed(selection)) if selection else [sequence[idx]]

    return zip(indices, reversed_selection)


def knot_hash(sequence: List[int], lengths: List[int], rounds: int = 1) -> List[int]:
    idx = skip = 0
    sequence_length = len(sequence)

    for _ in range(rounds):
        for knot_length in lengths:
            indices_section = reverse_section(sequence, idx, knot_length)

            for i, element in indices_section:
                sequence[i] = element

            idx = (idx+knot_length+skip) % sequence_length
            skip += 1

    return sequence


def knot_hash_hex(input_lengths: str, rounds: int) -> str:
    additional_lengths = [17, 31, 73, 47, 23]
    lengths = [CHAR_TO_ASCII[c] for c in input_lengths] + additional_lengths

    sparse_hash = knot_hash(list(range(256)), lengths, rounds)
    dense_hash = [
        functools.reduce(operator.xor, block)
        for block in sequence_blocks(sparse_hash, 16)
    ]
    hex_dense_hash = ''.join([f'{number:02x}' for number in dense_hash])

    return hex_dense_hash


if __name__ == '__main__':
    with open('data/day10.txt', 'rt') as f:
        lengths = [int(length) for length in f.read().strip().split(',')]

    test_output = knot_hash(TEST_LIST, TEST_LENGTHS)
    assert test_output[0]*test_output[1] == 12

    hash_output = knot_hash(list(range(256)), lengths)
    print(hash_output[0]*hash_output[1])

    # part two
    with open('data/day10.txt', 'rt') as f:
        int_lengths = f.read().strip()

    assert knot_hash_hex('', rounds=64) == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert knot_hash_hex('AoC 2017', rounds=64) == '33efeb34ea91902bb2f59c9920caa6cd'
    assert knot_hash_hex('1,2,3', rounds=64) == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert knot_hash_hex('1,2,4', rounds=64) == '63960835bcdc130f0b66d7ff4f6a5a8e'

    print(knot_hash_hex(int_lengths, rounds=64))
