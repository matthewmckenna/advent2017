#!/usr/bin/env python3
"""
Day 1 of the Advent of Code 2017 challenge.
"""
from aoc_utils import read_input_data


def inverse_captcha(input_data: str) -> int:
    """Inverse Captcha for Robots!

    Finds the sum of all digits that match the next digit in the
    sequence. This sequence of digits is circular.
    """
    summation = 0
    # since the sequence is circular, append the first element of
    # the data to the end of the list
    modified_input_data = input_data + input_data[0]

    for idx, value in enumerate(modified_input_data[1:], start=1):
        # is the current element equal to the previous one?
        if value == input_data[idx-1]:
            summation += int(value)

    return summation


def inverse_captcha_part_two(input_data: str) -> int:
    """Second part of the Inverse Captcha challenge.

    """
    summation = 0
    half_length = int(len(input_data) / 2)

    # since we need to look ahead `half_length` digits each check
    # we need to extend the list by `half_length`
    modified_input_data = input_data + input_data[:half_length]

    # in order to iterate over the original input data only we
    # should only enumerate up to the length of the original list.
    # alternatively, we could simply enumerate `input_data`
    for idx, value in enumerate(modified_input_data[:-half_length]):
        # check if the current value is equal to the one `half_length`
        # digits away
        if value == modified_input_data[idx+half_length]:
            summation += int(value)

    return summation


if __name__ == '__main__':
    input_data = read_input_data('data/day_one.txt')
    n_digits = 8
    print(f'displaying the first {n_digits} digits of the input')

    # part one
    for seq in ('1122', '1111', '1234', '91212129', input_data):
        output = inverse_captcha(seq)
        print(f'input={seq[:n_digits]} output={output}')

    print()

    # part two
    for seq in ('1212', '1221', '123425', '123123', '12131415', input_data):
        output = inverse_captcha_part_two(seq)
        print(f'input={seq[:n_digits]} output={output}')
