#!/usr/bin/env python3
"""
Day 3 of Avent of Code 2017.
http://adventofcode.com/2017/day/3
"""
from typing import List, Tuple
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23  24  25


def sum_adjacent():
    grid = generate_grid(rings=5)
    for ring in grid:
        print(ring)


def get_square_coords(square: int) -> Tuple[int, int]:
    grid = generate_grid(rings=310)
    coords = []

    for n, ring in enumerate(grid, start=1):
        diag = 2*n + 1

        xs, ys = [], []

        xs.extend([n] * (diag-2))
        xs.extend(range(n, -n-1, -1))
        xs.extend([-n] * (diag-2))
        xs.extend(range(-n, n+1))

        ys.extend(range(-n+1, n))
        ys.extend([n] * diag)
        ys.extend(range(-n+1, n))
        ys.extend([-n] * diag)

        coords.append(zip(xs, ys))

    if square == 1:
        return (0, 0)

    for i, ring in enumerate(grid):
        if square not in ring:
            continue

        idx = ring.index(square)
        return list(coords[i])[idx]


def generate_grid(rings: int) -> List[List[int]]:
    grid = []

    for n in range(1, rings+1):
        end = (2*n + 1)**2
        start = 2 if n == 1 else (2*(n-1) + 1)**2 + 1
        elements = list(range(start, end+1))

        grid.append(elements)

    return grid


def get_distance(square: int) -> int:
    coords = get_square_coords(square)
    return abs(coords[0]) + abs(coords[1])


if __name__ == '__main__':
    assert get_distance(1) == 0
    assert get_distance(12) == 3
    assert get_distance(23) == 2
    assert get_distance(1024) == 31
    assert get_distance(361527) == 326
    sum_adjacent()
