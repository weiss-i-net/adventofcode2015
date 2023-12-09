from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import operator as op
import math
import re

with open("input") as f:
    data = f.read().splitlines()

ingrediants = [ list(map(int, re.findall(r"-?\d+", line))) for line in data ]
part_1 = 0
part_2 = 0

for c1 in range(101):
    for c2 in range(101-c1):
        for c3 in range(101-c1-c2):
            c4 = 100-c1-c2-c3

            i1 = [ c1 * p for p in ingrediants[0] ]
            i2 = [ c2 * p for p in ingrediants[1] ]
            i3 = [ c3 * p for p in ingrediants[2] ]
            i4 = [ c4 * p for p in ingrediants[3] ]

            *scores, cals = (max(0, sum(p)) for p in zip(i1, i2, i3, i4))
            score = math.prod(scores)

            part_1 = max(part_1, score)
            if score > part_2 and cals == 500:
                part_2 = score

print(part_1)
print(part_2)
