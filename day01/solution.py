from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as it
import functools as func
import operator as op
import math
import re

with open("input") as f:
    data = f.read().splitlines()

c = Counter(data[0])
print(c["("] - c[")"])

floor = 0
for i, c in enumerate(data[0]):
    if c == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        print(i + 1)
        break

