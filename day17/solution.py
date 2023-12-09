from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import operator as op
import math
import re

def p(v):
    print(v)
    return v

with open("input") as f:
    data = list(map(int, f.read().splitlines()))

sample = [20, 15, 10, 5, 5]

print(sum(sum(c) == 25 for c in mit.powerset(sample)))
print(sum(sum(c) == 150 for c in mit.powerset(data)))

min_countainers = min(len(c) for c in mit.powerset(data) if sum(c) == 150)
print(sum(sum(c) == 150 for c in it.combinations(data, min_countainers)))
