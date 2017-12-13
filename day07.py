#!/usr/bin/env python3
"""
Day 7 of Advent of Code 2017.
http://adventofcode.com/2017/day/7
"""
from collections import defaultdict
from typing import DefaultDict, List, Set

from aoc_utils import flatten


def has_children(s: str) -> bool:
    return True if len(s.split()) > 2 else False


def get_children(node: str) -> List[str]:
    fields = node.replace(',', '').split()

    # field 0 is the parent, field 1 is the weight, field 2 is `->`
    children = fields[3:]

    return children


def get_parent(node: str) -> str:
    return node.split()[0]


def build_tree(nodes: List[str]) -> DefaultDict[str, List[str]]:
    tree: DefaultDict[str, List[str]] = defaultdict(list)

    for node in data:
        parent = get_parent(node)
        if has_children(node):
            children = get_children(node)
            tree[parent].extend(children)

    return tree


def is_child(node: str, children: Set[str]) -> bool:
    return True if node in children else False


def get_root_node(tree: DefaultDict[str, List[str]]) -> str:
    all_children = {v for v in flatten(tree.values())}

    for node in tree.keys():
        if not is_child(node, all_children):
            return node

    raise RuntimeError('No root node')


if __name__ == '__main__':
    with open('data/day07.txt', 'rt') as f:
        data = [line.strip('\n') for line in f]

    tree = build_tree(data)

    print(get_root_node(tree))
