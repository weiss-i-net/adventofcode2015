import itertools as it
import more_itertools as mit
import copy


with open("input") as f:
    grid = list(map(list, f.read().splitlines()))

N = len(grid)
for _ in range(100):
    new_grid = copy.deepcopy(grid)
    for x, y in it.product(range(N), repeat=2):
        neighbors = it.product(range(max(0, x-1), min(x+2, N)),
                               range(max(0, y-1), min(y+2, N)))
        neighbor_lights = sum(grid[s][t] == "#" for s, t in neighbors if (s, t) != (x, y))
        if grid[x][y] == "#" and neighbor_lights not in (2, 3):
            new_grid[x][y] = "."
        if grid[x][y] == "." and neighbor_lights == 3:
            new_grid[x][y] = "#"
    grid = new_grid

print("Part 1:", sum(l == "#" for l in mit.flatten(grid)))

with open("input") as f:
    grid = list(map(list, f.read().splitlines()))


for x, y in it.product((0, N-1), repeat=2):
    grid[x][y] = "#"
N = len(grid)
for x, y in it.product((0, N-1), repeat=2):
    grid[x][y] = "#"
for _ in range(100):
    new_grid = copy.deepcopy(grid)
    for x, y in it.product(range(N), repeat=2):
        neighbors = it.product(range(max(0, x-1), min(x+2, N)),
                               range(max(0, y-1), min(y+2, N)))
        neighbor_lights = sum(grid[s][t] == "#" for s, t in neighbors if (s, t) != (x, y))
        if grid[x][y] == "#" and neighbor_lights not in (2, 3):
            new_grid[x][y] = "."
        if grid[x][y] == "." and neighbor_lights == 3:
            new_grid[x][y] = "#"
    grid = new_grid
    for x, y in it.product((0, N-1), repeat=2):
        grid[x][y] = "#"

print("Part 2:", sum(l == "#" for l in mit.flatten(grid)))
