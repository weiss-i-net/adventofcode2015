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

adj = {}
all_f = 0xffff

for line in data:
    src, dest = line.split(" -> ")
    parts = src.split(" ")

    if len(parts) == 1:
        adj[dest] = ("ID", parts[0])
    elif len(parts) == 2:
        adj[dest] = ("NOT", parts[1])
    else:
        a, op, b = parts
        adj[dest] = (op, a, b)

@func.cache
def get_val(a):
    if a.isdigit():
        return int(a)

    op, *bs = adj[a]
    if op == "ID":
        return get_val(bs[0])
    elif op == "NOT":
        return all_f ^ get_val(bs[0])
    elif op == "AND":
        return get_val(bs[0]) & get_val(bs[1])
    elif op == "OR":
        return get_val(bs[0]) | get_val(bs[1])
    elif op == "LSHIFT":
        return all_f & (get_val(bs[0]) << int(bs[1]))
    elif op == "RSHIFT":
        return all_f & (get_val(bs[0]) >> int(bs[1]))

part_1 = get_val("a")

adj["b"] = ("ID", str(part_1))
get_val.cache_clear()
part_2 = get_val("a")

print(part_1)
print(part_2)
