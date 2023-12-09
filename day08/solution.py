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

part_1 = 0
part_2 = 0
for line in data:
    exec("string = " + line)
    part_1 += len(line) - len(string)
    c = Counter(line)
    part_2 += c["\\"] + c['"'] + 2


print(part_1)
print(part_2)

