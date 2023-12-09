from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import operator as op
import math
import re
import sympy
from tqdm import tqdm

def p(v):
    print(v)
    return v

num = 33100000

max_house = num // 25

houses = [0] * max_house
for i in tqdm(range(1, max_house)):
    for j in range(i, max_house, i):
        houses[j] += i

print("Part 1:", next(i for i, p in enumerate(houses) if 10*p >= num))


houses = [0] * max_house
for i in tqdm(range(1, max_house)):
    for j in range(1, 51):
        if i*j >= max_house:
            break
        houses[j*i] += i

print("Part 2:", next(i for i, p in enumerate(houses) if 11*p >= num))
