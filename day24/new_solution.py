import more_itertools as mit
import math

def find_min_entagelment(packages, num_groups):
    group_weight = sum(packages) // num_groups

    def rest(group):
        return [ p for p in packages if p not in group ]
    def groups(packages):
        for group in mit.powerset(packages):
            if sum(group) == group_weight:
                yield group
    def can_group(packages, num_groups):
        if num_groups == 1:
            return True
        return any(can_group(rest(g), num_groups-1) for g in groups(packages))

    min_entagelment = math.inf
    min_group_size = math.inf
    for group in groups(packages):
        if not can_group(rest(group), num_groups-1):
            continue
        if len(group) > min_group_size:
            break
        min_group_size = len(group)
        min_entagelment = min(min_entagelment, math.prod(group))
    return min_entagelment

with open("input") as f:
    data = f.read().splitlines()
packages = list(map(int, data))

print(find_min_entagelment(packages, 3))
print(find_min_entagelment(packages, 4))
