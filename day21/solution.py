import itertools as it

boss_health = 104
boss_dmg = 8
boss_armor = 1

store_string = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""


sections = [ s.splitlines()[1:] for s in store_string.split("\n\n") ]

weapons = [ list(map(int, line.split()[1:])) for line in sections[0] ]
armor   = [ list(map(int, line.split()[1:])) for line in sections[1] ]
rings   = [ list(map(int, line.split()[2:])) for line in sections[2] ]

min_cost = float("inf")
max_cost = 0

for w_c, w_d, w_a in weapons:
    for has_armor in range(2):
        for a_c, a_d, a_a in armor if has_armor else ((0, 0, 0),):
            for ring_count in range(3):
                for rs in it.combinations(rings, ring_count):
                    if rs:
                        r_c, r_d, r_a = map(sum, zip(*rs))
                    else:
                        r_c, r_d, r_a = 0, 0, 0

                    cost         = w_c + a_c + r_c
                    player_dmg   = w_d + a_d + r_d
                    player_armor = w_a + a_a + r_a

                    player_h = 100
                    boss_h = boss_health

                    players_turn = True
                    while boss_h > 0 and player_h > 0:
                        if players_turn:
                            boss_h -= max(0, player_dmg - boss_armor)
                        else:
                            player_h -= max(0, boss_dmg - player_armor)
                        players_turn ^= 1
                    if player_h > 0:
                        min_cost = min(min_cost, cost)
                    else:
                        max_cost = max(max_cost, cost)

print("Part 1:", min_cost)
print("Part 2:", max_cost)
