from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import operator as op
import math
import re
import json


with open("input") as f:
    data = json.load(f)

def part_1(d):
    if type(d) is int:
        return d
    if type(d) is list:
        return sum(map(part_1, d))
    if type(d) is dict:
        return sum(map(part_1, d.values()))
    return 0

def part_2(d):
    if type(d) is int:
        return d
    if type(d) is list:
        return sum(map(part_2, d))
    if type(d) is dict and "red" not in d.values():
        return sum(map(part_2, d.values()))
    return 0

print(part_1(data))
print(part_2(data))


