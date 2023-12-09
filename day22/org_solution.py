
import math
import functools as fun

@fun.cache
def mana_cost(player_mana, player_hp, boss_hp, shield, poison, recharge, player_turn):
    if player_hp <= 0:
        return math.inf
    if poison > 0:
        boss_hp -= 3
    if recharge > 0:
        player_mana += 101
    if boss_hp <= 0:
        return 0
    if not player_turn:
        player_hp -= 1 if shield > 0 else 8
        return mana_cost(player_mana, player_hp, boss_hp, shield-1, poison-1, recharge-1, True)
    costs = []
    costs.append(53 + mana_cost(player_mana-53, player_hp, boss_hp-4, shield-1, poison-1, recharge-1, False))
    costs.append(73 + mana_cost(player_mana-73, player_hp+2, boss_hp-2, shield-1, poison-1, recharge-1, False))
    if shield <= 1:
        costs.append(113 + mana_cost(player_mana-113, player_hp, boss_hp, 6, poison-1, recharge-1, False))
    if poison <= 1:
        costs.append(173 + mana_cost(player_mana-173, player_hp, boss_hp, shield-1, 6, recharge-1, False))
    if recharge <= 1:
        costs.append(229 + mana_cost(player_mana-229, player_hp, boss_hp, shield-1, poison-1, 5, False))
    return min(costs)

print(mana_cost(50, 50, 58, 0, 0, 0, True))
