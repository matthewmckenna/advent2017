#!/usr/bin/env python3
"""
Day 11 of Advent of Code 2017.
http://adventofcode.com/2017/day/11
"""
from collections import Counter
from typing import List, Tuple

from aoc_utils import read_input_data


COMBINING_TERMS = {
    ('n', 'se'): 'ne',
    ('ne', 's'): 'se',
    ('se', 'sw'): 's',
    ('s', 'nw'): 'sw',
    ('sw', 'n'): 'nw',
    ('nw', 'ne'): 'n',
}


def cancel_terms(l: List[str], pairs: List[Tuple[str, str]], combine: bool = False) -> List[str]:
    for pair in pairs:
        c = Counter(l)
        terms = min(c[pair[0]], c[pair[1]])

        for _ in range(terms):
            l.remove(pair[0])
            l.remove(pair[1])
            if combine:
                l.append(COMBINING_TERMS[pair])

    return l


def reduce_terms(s: str) -> str:
    input_list = s.split(',')

    working_list = cancel_terms(input_list, [('n', 's'), ('ne', 'sw'), ('se', 'nw')])
    working_list = cancel_terms(working_list, list(COMBINING_TERMS.keys()), combine=True)

    return ','.join(working_list)


def how_many_steps(s: str) -> int:
    reduced_steps = reduce_terms(s)

    if reduced_steps == '':
        return 0

    return len(reduced_steps.split(','))


def furthest_ever(s: str) -> int:
    max_steps = 0
    moves = s.split(',')

    for i, move in enumerate(moves):
        steps = how_many_steps(','.join(moves[:i]))
        max_steps = max(steps, max_steps)

    return max_steps


if __name__ == '__main__':
    directions = read_input_data('data/day11.txt')

    assert how_many_steps('ne,ne,ne') == 3
    assert how_many_steps('ne,ne,sw,sw') == 0
    assert how_many_steps('ne,ne,s,s') == 2
    assert how_many_steps('se,sw,se,sw,sw') == 3

    print(how_many_steps(directions))
    print(furthest_ever(directions))
