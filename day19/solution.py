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

sample = """e => H
e => O
H => HO
H => OH
O => HH

HOH""".splitlines()

string = data[-1]
mol = list(re.findall(r"[A-Z][a-z]?", string))
reactions = defaultdict(list)

possible_strings = set()

for line in data[:-2]:
    a, bs = line.split(" => ")
    bs = list(re.findall(r"[A-Z][a-z]?", bs))
    reactions[a].append(bs)
    for i, e in enumerate(mol):
        if a == e:
            new_mol = mol[:i] + bs + mol[i+1:]
            possible_strings.add("".join(new_mol))
print("Part 1:", len(possible_strings))

# patterns:
# X => XX              #1 = ?
# X => X Rn X Ar       #2 = #Rn - #Y
# X => X Rn X Y X Ar   #3 = #Y
#
# (Rn, Y, Ar are terminals)

#    N = 1 + #1 + #2*3 + #3*5
# -> #1 = N - 1 - #2*3 - #3*5
# -> #1 + #2 + #3 = N - 1 - #2*2 - #3*4 = N - 1 - 2*(#Rn - #Y) - 4*#Y = N - 1 - 2*#Rn -2*#Y

print("Part 2:", len(mol) - 1 - 2*mol.count("Rn") - 2*mol.count("Y"))



"""
goal = mol
mols = [ [ "e" ] ]
for iterations in it.count():
    print(iterations, len(mols))
    next_mols = []
    while mols:
        mol = mols.pop()
        if len(mol) > len(goal):
            continue
        if mol == goal:
            print("done", iterations)
            exit()
        for i, m in enumerate(mol):
            for k in reactions[m]:
                next_mols.append(mol[:i] + k + mol[i+1:])
    mols = list(mit.unique_everseen(next_mols, key=tuple))
    print(len(mols[0]), len(goal))
    #mols = list(map(list, set(map(tuple, next_mols))))

"""

