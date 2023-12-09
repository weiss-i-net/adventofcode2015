from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import operator as op
import math
import re

with open("input") as f:
    data = f.read().splitlines()


part_1 = 0
for line in data:
    c = Counter(line)
    if sum(c[v] for v in "aeiou") < 3:
        continue
    if not any(a == b for a, b in it.pairwise(line)):
        continue
    if any(pair in line for pair in ["ab", "cd", "pq", "xy"]):
        continue
    part_1 += 1

part_2 = 0
for line in data:
    double_pair = False
    for i, p in enumerate(it.pairwise(line)):
        for j, q in enumerate(it.pairwise(line)):
            if p == q and i - j > 1:
                double_pair = True
    if not double_pair:
        continue
    if not any(a == c for a, b, c in mit.windowed(line, 3)):
        continue
    part_2 += 1


print(part_1)
print(part_2)

