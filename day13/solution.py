from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import operator as op
import math
import re
import networkx as nx
import matplotlib.pyplot as plt

with open("input") as f:
    data = f.read().splitlines()

G = nx.Graph()
for line in data:
    line = line.split()
    person_a = line[0]
    person_b = line[-1][:-1]
    sign = 1 if line[2] == "gain" else -1
    points = sign * int(line[3])
    if G.has_edge(person_a, person_b):
        G[person_a][person_b]['h'] += points
    else:
        G.add_edge(person_a, person_b, h=points)

part_1 = max(nx.path_weight(G, p + (p[0],), 'h') for p in it.permutations(G.nodes))
for person in list(G.nodes):
    G.add_edge("I", person, h=0)

part_2 = max(nx.path_weight(G, p + (p[0],), 'h') for p in it.permutations(G.nodes))
print(part_1)
print(part_2)

