#!/usr/bin/env python3
"""
Day 9 of Advent of Code 2017.
http://adventofcode.com/2017/day/9
"""

from aoc_utils import read_input_data


def count_groups(stream: str) -> int:
    group_started = True
    inside_garbage = False
    complete_groups = 0

    for idx, character in enumerate(stream[1:]):
        if stream[idx-1] == '!':
            continue

        if not inside_garbage and character == '<':
            inside_garbage = True

        if inside_garbage and character == '>':
            inside_garbage = False

        if character == '}' and not inside_garbage and group_started:
            complete_groups += 1

    return complete_groups


def get_stream_score(stream: str) -> int:
    group_started = True
    inside_garbage = previous_bang = False
    complete_groups = score = 0
    group_score = 1

    for idx, character in enumerate(stream[1:], start=1):
        if stream[idx-1] == '!' and not previous_bang:
            previous_bang = True
            continue

        if not inside_garbage and character == '<':
            inside_garbage = True

        if inside_garbage and character == '>':
            inside_garbage = False

        if character == '{' and not inside_garbage:
            group_score += 1

        if character == '}' and not inside_garbage and group_started:
            complete_groups += 1
            score += group_score
            group_score -= 1

        # reset this variable
        previous_bang = False

    return score


def count_garbage_characters(stream: str) -> int:
    garbage_characters = 0
    inside_garbage = previous_bang = False

    for idx, character in enumerate(stream):
        if idx != 0 and stream[idx-1] == '!' and not previous_bang:
            previous_bang = True
            continue

        if inside_garbage and character == '>':
            inside_garbage = False

        if inside_garbage:
            if character != '!':
                garbage_characters += 1

        if not inside_garbage and character == '<':
            inside_garbage = True

        # reset this variable
        previous_bang = False

    return garbage_characters


GROUPS_INPUT_COUNTS = {
    '{}': 1,
    '{{{}}}': 3,
    '{{},{}}': 3,
    '{{{},{},{{}}}}': 6,
    '{<{},{},{{}}>}': 1,
    '{<a>,<a>,<a>,<a>}': 1,
    '{{<a>},{<a>},{<a>},{<a>}}': 5,
    '{{<!>},{<!>},{<!>},{<a>}}': 2,
}

SCORE_INPUT_COUNTS = {
    '{}': 1,
    '{{{}}}': 6,
    '{{},{}}': 5,
    '{{{},{},{{}}}}': 16,
    '{<a>,<a>,<a>,<a>}': 1,
    '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
    '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
    '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3,
}

GARBAGE_CHAR_COUNTS = {
    '<>': 0,
    '<random characters>': 17,
    '<<<<>': 3,
    '<{!>}>': 2,
    '<!!>': 0,
    '<!!!>>': 0,
    '<{o"i!a,<{i<a>': 10,
}

if __name__ == '__main__':
    for stream, count in GROUPS_INPUT_COUNTS.items():
        assert count_groups(stream) == count

    for stream, score in SCORE_INPUT_COUNTS.items():
        assert get_stream_score(stream) == score

    for stream, count in GARBAGE_CHAR_COUNTS.items():
        assert count_garbage_characters(stream) == count

    stream = read_input_data('data/day09.txt')

    print(get_stream_score(stream))
    print(count_garbage_characters(stream))
