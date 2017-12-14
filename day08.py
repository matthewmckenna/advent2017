#!/usr/bin/env python3
"""
Day 8 of Advent of Code 2017.
http://adventofcode.com/2017/day/8
"""
from collections import defaultdict
from typing import DefaultDict, Iterable, Tuple

from aoc_utils import yield_lines

TEST_DATA = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""


def split_instruction(instruction: str) -> Tuple[str, str, int, str]:
    fields = instruction.split()
    register = fields[0]
    inc_dec = fields[1]
    amount = int(fields[2])
    condition = ' '.join(fields[4:])

    return (register, inc_dec, amount, condition)


def check_condition(registers: DefaultDict[str, int], condition: str) -> bool:
    register, operator, str_value = condition.split()
    value = int(str_value)

    return {
        '>': registers[register] > value,
        '>=': registers[register] >= value,
        '<': registers[register] < value,
        '<=': registers[register] <= value,
        '==': registers[register] == value,
        '!=': registers[register] != value,
    }.get(operator, False)


def process_instructions(instructions: Iterable[str]) -> DefaultDict[str, int]:
    instructions = instructions
    registers: DefaultDict[str, int] = defaultdict(int)

    for instruction in instructions:
        register, inc_dec, amount, condition = split_instruction(instruction)
        if check_condition(registers, condition):
            if inc_dec == 'inc':
                registers[register] += amount
            else:
                registers[register] -= amount

    return registers


def highest_value_held(instructions: Iterable[str]) -> int:
    registers: DefaultDict[str, int] = defaultdict(int)
    highest_value = 0

    for instruction in instructions:
        register, inc_dec, amount, condition = split_instruction(instruction)
        if check_condition(registers, condition):
            if inc_dec == 'inc':
                registers[register] += amount
            else:
                registers[register] -= amount

        registers_max = max(registers.values())
        if registers_max > highest_value:
            highest_value = registers_max

    return highest_value


if __name__ == '__main__':
    filename = 'data/day08.txt'
    test_lines = TEST_DATA.split('\n')
    assert max(process_instructions(test_lines).values()) == 1
    assert highest_value_held(test_lines) == 10

    lines = yield_lines(filename)
    registers = process_instructions(lines)
    print(max(registers.values()))

    # read the lines again as the iterator was exhausted
    lines = yield_lines(filename)
    print(highest_value_held(lines))
