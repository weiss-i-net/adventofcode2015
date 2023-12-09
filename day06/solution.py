from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import operator as op
import math
import re

with open("input") as f:
    data = f.read().splitlines()

grid = [ [0] * 1000 for _ in range(1000) ]
b_grid = [ [0] * 1000 for _ in range(1000) ]

for line in data:
    words = line.split(" ")
    x, y = map(int, words[-3].split(","))
    i, j = map(int, words[-1].split(","))
    for s, t in it.product(range(x, i+1), range(y, j+1)):
        if words[0] == "toggle":
            grid[s][t] ^= 1
            b_grid[s][t] += 2
        elif words[1] == "on":
            grid[s][t] = 1
            b_grid[s][t] += 1
        elif words[1] == "off":
            grid[s][t] = 0
            b_grid[s][t] = max(0, b_grid[s][t]-1)

print(sum(map(sum, grid)))
print(sum(map(sum, b_grid)))
