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
    data = f.read().splitlines()

packages = list(map(int, data))

def partitions(elems, *sums):
    if len(elems) == 3:
        if all(e == s for e, s in zip(elems, sums)):
            yield tuple((elem,) for elem in elems)
        return
    for i in range(3):
        if sums[i] - elems[0] < 9:
            continue
        new_sums = list(sums)
        new_sums[i] -= elems[0]
        for partition in partitions(elems[1:], *new_sums):
            yield partition[:i] + ((elems[0],) + partition[i],) + partition[i+1:]

sample = tuple(range(1, 6)) + tuple(range(7, 12))
sample_sum = sum(sample) // 3
print(list(partitions(sample, sample_sum, sample_sum, sample_sum)))
# not feasable

packages = sample

minimal_count = math.inf
minimal_entangelment = math.inf
subset_sum = sum(packages) // 3
for a, b, c in partitions(packages, subset_sum, subset_sum, subset_sum):
    if len(a) < minimal_count:
        minimal_count = len(a)
        minimal_entangelment = math.prod(a)
    elif len(a) == minimal_count:
        minimal_entangelment = min(minimal_entangelment, math.prod(a))


print(minimal_entangelment)
