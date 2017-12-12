#!/usr/bin/env python3
"""
Day 3 of Avent of Code 2017.
http://adventofcode.com/2017/day/3
"""
from typing import List, Tuple
import itertools
from aoc_utils import flatten
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23  24  25

DIRECTION_TO_COORDS = {
    'N': (0, 1),
    'NE': (1, 1),
    'E': (1, 0),
    'SE': (1, -1),
    'S': (0, -1),
    'SW': (-1, -1),
    'W': (-1, 0),
    'NW': (-1, 1),
}

SIDES = {
    0: [('W', 'NW'), ('S', 'SW', 'W', 'NW'), ('S', 'SW', 'W'), ('S', 'SW')],
    1: [('E', 'SE', 'S', 'SW'), ('E', 'SE', 'S'), ('E', 'SE')],
    2: [('N', 'NE', 'E', 'SE'), ('N', 'NE', 'E'), ('N', 'NE')],
    3: [('N', 'NE', 'W', 'NW'), ('N', 'W', 'NW')],
}

RING1_SIDES = {
    0: [('W'), ('S', 'SW')],
    1: [('E', 'SE', 'S'), ('E', 'SE')],
    2: [('N', 'NE', 'E'), ('N', 'NE')],
    3: [('N', 'NE', 'W', 'NW'), ('N', 'W', 'NW')],
}

CENTRE_VALUE = 1


def sum_adjacent(target_value: int) -> int:
    # number of values to generate
    max_value = 70
    # number of rings to generate
    # each ring contains (2*n + 1)**2 elements
    max_rings = 10

    # get a grid
    grid = generate_grid(rings=max_rings)
    # get coordinates relative to the centre for each grid index
    grid_coords = [get_grid_coords(ring) for ring in grid]

    # flatten the coordinates into a one-dimensional list
    flat_coords = list(flatten(grid_coords))

    # initialise with the value ``1`` in the centre
    values = [CENTRE_VALUE]

    # build mappings from indices to coordinates and vice versa
    coords_to_idx = {(x, y): idx for idx, (x, y) in enumerate(flat_coords, start=1)}
    idx_to_coords = {idx: (x, y) for idx, (x, y) in enumerate(flat_coords, start=1)}

    # add the zero cases
    coords_to_idx[(0, 0)] = 0
    idx_to_coords[0] = (0, 0)

    # each ring starts on an odd square (9, 25, 49, 81, etc.)
    ring_start_indices = [x ** 2 for x in range(3, max_value, 2)]

    # initialise some variables to keep track of where we are
    last_ring = index_in_ring = side = index_in_side = 0

    for i in range(1, max_value):
        # get the ring number for the current ``i``
        ring_idx = get_ring_index(i, ring_start_indices)

        # update some variables if we've moved on to a new ring
        if ring_idx != last_ring:
            last_ring = ring_idx
            index_in_ring = 0
            index_in_side = 0
            side = 0

        num_values_on_side = ring_idx * 2

        # take note if we change side within a ring
        if index_in_ring != 0 and index_in_ring % num_values_on_side == 0:
            side += 1
            index_in_side = 0

        # the valid neighbours for each location have been computed
        # offline by looking at the sample input.
        # the case for ring 1 differs slightly, and so select the
        # appropriate dictionary
        sides = RING1_SIDES if i < 9 else SIDES

        # get the index into the directions list depending on the
        # index of the square within the ring
        if ring_idx == 1:
            directions_idx = index_in_ring % num_values_on_side
        else:
            if index_in_side == 0:
                directions_idx = 0
            elif index_in_side == num_values_on_side-1:
                directions_idx = -1
            elif index_in_side == num_values_on_side-2:
                directions_idx = -2
            else:
                directions_idx = 1 if side == 0 else 0

        this_coords = idx_to_coords[i]
        neighbours = sides[side][directions_idx]

        total = 0
        for neighbour in neighbours:
            x = this_coords[0] + DIRECTION_TO_COORDS[neighbour][0]
            y = this_coords[1] + DIRECTION_TO_COORDS[neighbour][1]
            total += (values[coords_to_idx[(x, y)]])

        values.append(total)

        index_in_ring += 1
        index_in_side += 1

        if values[-1] > target_value:
            return values[-1]


def get_ring_index(square: int, start_indices: List[int]) -> int:
    """Get the ring index from a square index."""
    if square == 0:
        raise ValueError('Invalid square number.')

    if square < 9:
        return 1

    # linear search, but it doesn't matter for now
    for i, value in enumerate(start_indices):
        if square < value:
            return i+1


def get_grid_coords(ring: List[int]) -> List[Tuple[int, int]]:
    """Takes a ring of indexes and returns coords from centre tile.
    """
    # n is the index of the ring, e.g., ring 1, ring 2, etc.
    n = len(ring) // 8

    diag = 2*n + 1

    xs, ys = [], []

    xs.extend([n] * (diag-2))
    xs.extend(range(n, -n-1, -1))
    xs.extend([-n] * (diag-2))
    xs.extend(range(-n, n+1))

    # print(len(xs))

    ys.extend(range(-n+1, n))
    ys.extend([n] * diag)
    ys.extend(range(n-1, -n, -1))
    ys.extend([-n] * diag)
    # print(len(ys))

    coords = list(zip(xs, ys))

    return coords


def get_square_coords(grid: List[List[int]], square: int) -> Tuple[int, int]:
    grid_coords = [get_grid_coords(ring) for ring in grid]

    if square <= 0:
        raise ValueError('Invalid square index.')

    if square == 1:
        return (0, 0)

    flat_coords = flatten(grid_coords)

    return tuple(itertools.islice(flat_coords, square-2, square-1))[0]


def generate_grid(rings: int) -> List[List[int]]:
    grid = []

    for n in range(1, rings+1):
        end = (2*n + 1)**2
        start = 2 if n == 1 else (2*(n-1) + 1)**2 + 1
        elements = list(range(start, end+1))

        grid.append(elements)

    return grid


def get_distance(square: int) -> int:
    grid = generate_grid(rings=310)
    coords = get_square_coords(grid, square)
    x, y = coords
    return abs(x) + abs(y)


if __name__ == '__main__':
    assert get_distance(1) == 0
    assert get_distance(12) == 3
    assert get_distance(23) == 2
    assert get_distance(1024) == 31

    print(sum_adjacent(361527))
