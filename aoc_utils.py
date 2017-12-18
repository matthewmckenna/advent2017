#!/usr/bin/env python3
"""
some utility functions for the advent of code 2017 challenge.
"""
import csv
from typing import Any, Iterable, List, Reversible, Sized
import itertools


class IterableSequence(Reversible, Sized):
    """Custom type that supports `len()` and `reversed()` functions."""


def read_input_data(filename: str) -> str:
    """Takes a filename and returns a string representation of the data."""
    with open(filename, 'rt') as f:
        data = f.read().strip()
    return data


def read_tsv(filename: str) -> List[List[str]]:
    """Reads a TSV file and returns a list of lists of strings."""
    with open(filename, 'rt') as f:
        reader = csv.reader(f, delimiter='\t')
        rows = [row for row in reader]

    return rows


def yield_lines(filename: str) -> Iterable[str]:
    with open(filename, 'rt') as f:
        for line in f:
            yield line.strip()


def flatten(iterable: Iterable[Iterable[Any]]) -> Iterable[Any]:
    """Flattens one level of nesting within an iterable."""
    return itertools.chain.from_iterable(iterable)


def reverse_enumerate(iterable: IterableSequence) -> Iterable[Any]:
    """Get an iterable which can be traversed and enumerated in reverse order."""
    return zip(range(len(iterable)-1, -1, -1), reversed(iterable))


def sequence_blocks(sequence: List, blocksize: int) -> Iterable:
    """Yield evenly sized blocks from a sequence."""
    for i in range(0, len(sequence), blocksize):
        yield sequence[i:i+blocksize]
