from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import operator as op
import math
import re

with open("input") as f:
    data = f.read().splitlines()

santa_seen      = set([(0,0)])
robo_santa_seen = set([(0,0)])

x, y = 0, 0
s, t = 0, 0

move = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (1, 0),
    "v": (-1, 0),
}

for d, q in mit.chunked(data[0], 2):
    x += move[d][0]
    y += move[d][1]
    s += move[q][0]
    t += move[q][1]

    santa_seen.add((x, y))
    robo_santa_seen.add((s, t))

print(len(santa_seen))
print(len(santa_seen | robo_santa_seen))
