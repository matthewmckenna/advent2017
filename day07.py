#!/usr/bin/env python3
"""
Day 7 of Advent of Code 2017.
http://adventofcode.com/2017/day/7
"""
from collections import Counter, defaultdict
from typing import DefaultDict, Dict, List, Set, Tuple

from aoc_utils import flatten


Tree = DefaultDict[str, List[str]]


def has_children(s: str) -> bool:
    return True if len(s.split()) > 2 else False


def get_children(node: str) -> List[str]:
    fields = node.replace(',', '').split()

    # field 0 is the parent, field 1 is the weight, field 2 is `->`
    children = fields[3:]

    return children


def get_parent(node: str) -> str:
    return node.split()[0]


def build_weight_lookup(nodes: List[str]) -> Dict[str, int]:
    name_weight: Dict[str, int] = {}

    for node in nodes:
        # strip parentheses and split
        fields = node.replace('(', '').replace(')', '').split()

        # field 0 is the node name, and field 1 is the weight
        name_weight[fields[0]] = int(fields[1])

    return name_weight


def build_tree(nodes: List[str]) -> Tree:
    tree: DefaultDict[str, List[str]] = defaultdict(list)

    for node in data:
        parent = get_parent(node)
        if has_children(node):
            children = get_children(node)
            tree[parent].extend(children)

    return tree


def is_child(node: str, children: Set[str]) -> bool:
    return True if node in children else False


def get_root_node(tree: Tree) -> str:
    all_children = {v for v in flatten(tree.values())}

    for node in tree.keys():
        if not is_child(node, all_children):
            return node

    raise RuntimeError('No root node')


# def get_child_weights(tree: Tree, weights: Dict[str, int]) -> Dict[str, int]:
#     child_weights: Dict[str, int] = {}
#     for node, children in tree.items():
#         child_weights[node] = sum((weights[c] for c in children)) + weights[node]
#
#     return child_weights


def get_weights_recursive(tree: Tree, weights: Dict[str, int], node: str, w: int = 0) -> int:
    if node in tree:
        children = tree[node]
        w += sum((get_weights_recursive(tree, weights, c, w) for c in children))
    else:
        return weights[node]

    return w + weights[node]


def get_weight_difference(nodes_and_weights: List[Tuple[str, int]]) -> int:
    branch_weights = [w for _, w in nodes_and_weights]
    return max(branch_weights) - min(branch_weights)


def get_bad_node(nodes_and_weights: List[Tuple[str, int]]) -> str:
    branch_weights = [w for _, w in nodes_and_weights]
    c = Counter(branch_weights)
    frequencies = c.most_common()

    bad_weight = frequencies[-1][0]

    return nodes_and_weights[branch_weights.index(bad_weight)][0]


def all_nodes_balanced(nodes_and_weights: List[Tuple[str, int]]) -> bool:
    weights = [w for _, w in nodes_and_weights]
    return True if len(set(weights)) == 1 else False


def get_correct_weight(node: str, tree: Tree, weights: Dict[str, int]) -> int:
    imbalanced_branches = True
    weight_difference = 0

    while imbalanced_branches:
        nodes_and_weights = [
            (c, get_weights_recursive(tree, weights, c))
            for c in tree[node]
        ]

        if not all_nodes_balanced(nodes_and_weights):
            node = get_bad_node(nodes_and_weights)
            weight_difference = get_weight_difference(nodes_and_weights)
        else:
            break

    return weights[node]-weight_difference


if __name__ == '__main__':
    with open('data/day07.txt', 'rt') as f:
        data = [line.strip('\n') for line in f]

    tree = build_tree(data)

    root_node = get_root_node(tree)
    print(f'root_node={root_node}')

    weights = build_weight_lookup(data)

    correct_weight = get_correct_weight(root_node, tree, weights)
    print(f'correct_weight={correct_weight}')
