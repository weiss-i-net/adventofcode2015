from collections import Counter, defaultdict, deque
import itertools as it
import more_itertools as mit
import functools as func
import operator as op
import math
import re
import networkx as nx

def p(v):
    print(v)
    return v

with open("input") as f:
    data = f.read().splitlines()

graph = nx.Graph()
for line in data:
    city_a, _, city_b, _, dist = line.split(" ")
    graph.add_edge(city_a, city_b, dist=int(dist))


print(min(nx.path_weight(graph, path, "dist") for path in it.permutations(graph.nodes)))
print(max(nx.path_weight(graph, path, "dist") for path in it.permutations(graph.nodes)))
