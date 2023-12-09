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

reindeer = []
max_distance = 0
for line in data:
    speed, duration, rest = map(int, re.findall(r"\d+", line))
    reindeer.append((speed, duration, rest))
    cycles, rest = divmod(2503, duration + rest)
    distance = cycles * speed * duration + speed * min(rest, duration)
    max_distance = max(distance, max_distance)
print(max_distance)

points = [0] * len(reindeer)
for i in range(1, 2504):
    max_distance = 0
    best = []

    for j, (speed, duration, rest) in enumerate(reindeer):
        cycles, rest = divmod(i, duration + rest)
        distance = cycles * speed * duration + speed * min(rest, duration)
        if distance == max_distance:
            best.append(j)
        if distance > max_distance:
            max_distance = distance
            best = [ j ]

    for i in best:
        points[i] += 1

print(max(points))

