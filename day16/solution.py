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

ticker_tape = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

known = dict(line.split(": ") for line in ticker_tape.splitlines())

for line in data:
    right_sue_1 = True
    right_sue_2 = True
    sue, items = line.split(": ", 1)
    for item in items.split(", "):
        name, count = item.split(": ")
        if name not in known:
            continue

        if known[name] != count:
            right_sue_1 = False

        if name in ("cats", "trees"):
            if int(known[name]) >= int(count):
                right_sue_2 = False
        elif name in ("pomeranians", "goldfish"):
            if int(known[name]) <= int(count):
                right_sue_2 = False
        elif known[name] != count:
            right_sue_2 = False

    if right_sue_1:
        print(f"Part 1: {sue}")
    if right_sue_2:
        print(f"Part 2: {sue}")
