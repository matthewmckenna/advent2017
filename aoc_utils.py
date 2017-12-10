#!/usr/bin/env python3
"""
some utility functions for the advent of code 2017 challenge.
"""
import csv
from typing import List


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
