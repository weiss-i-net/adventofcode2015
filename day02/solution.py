from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as it
import functools as func
import operator as op
import math
import re

with open("input") as f:
    data = f.read().splitlines()

part_1 = 0
part_2 = 0
for line in data:
    l, w, h = map(int, line.split("x"))
    part_1 += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, l*h)
    part_2 += l*w*h + min(l+w, w+h, l+h)*2

print(part_1)
print(part_2)
